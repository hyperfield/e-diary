from datacenter.models import Mark
from datacenter.models import Schoolkid
from datacenter.models import Chastisement
from datacenter.models import Subject
from datacenter.models import Commendation
from datacenter.models import Teacher
from datacenter.models import Lesson
from django.core.exceptions import ObjectDoesNotExist
import datetime
import random


def fix_marks(name):
    """Удаляет "2" и "3", заменяя их на "4" или "5" в случайном порядке.

    Функция удаляет неправильные оценки из электронного дневника,
    заменяя их на правильные.

    Пример использования: fix_marks('Фролов Иван Григорьевич')
    """
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
        bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
        for mark in bad_marks:
            if mark.points <= 3:
                mark.points = random.choice([4, 5])
                mark.save()
        print("Оценки исправлены!")
    except ObjectDoesNotExist:
        print(f"Запись с именем {name} не найдена!")
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько записей с именем {name}!")


def remove_chastisements(name):
    """Функция по удалению замечаний из дневника.
    
    Пример использования: remove_chastisements("Фролов Иван Григорьевич")
    """
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
        chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
        chastisements.delete()
        print("Замечания удалены!")
    except ObjectDoesNotExist:
        print(f"Запись с именем {name} не найдена!")
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько записей с именем {name}!")


def get_lessons(lessons, date):
    """Поиск урока в списке уроков по его дате.

    Функция ищет по списку уроков и возвращает урок,
    соответствующий заданонй дате.

    Пример использования: get_lessons(lessons, datetime.datetime(2018, 4, 30))
    """
    found_lesson = None
    for lesson in lessons:
        if lesson.date == date:
            found_lesson = lesson
            break
    if found_lesson is not None:
        return found_lesson
    else:
        return "Урок не найден!"


def create_commendation(name, subject_name, subject_year, commendation,
                        teacher_name, date):
    """Создаёт похвалу в электронном дневнике по определенному уроку.

    Пример использования:
    name = "Фролов Иван Григорьевич"
    teacher_name = "Котов Флорентин"
    subject_name = "Математика"
    subject_year = 6
    commendation = "С каждым разом у тебя получается всё лучше!"
    create_commendation(name, subject_name, subject_year, commendation,
                        teacher_name, date)
    """
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
    except ObjectDoesNotExist:
        print(f"Запись с именем {name} не найдена!")
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько записей с именем {name}!")

    try:
        subject = Subject.objects.get(title__contains=subject_name,
                                      year_of_study=subject_year)
    except ObjectDoesNotExist:
        print(f"Запись с названием {subject_name} и город {subject_year}"
              + "не найдена!")

    try:
        teacher = Teacher.objects.get(full_name__contains=teacher_name)
    except ObjectDoesNotExist:
        print(f"Запись с именем {teacher_name} не найдена!")
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько записей с именем {teacher_name}!")

    try:
        lesson = Lesson.objects.get(subject=subject, teacher=teacher,
                                    date=date)
        Commendation.objects.create(teacher=lesson.teacher,
                                    text=commendation,
                                    schoolkid=schoolkid,
                                    subject=lesson.subject,
                                    created=lesson.date)
        print("Похвала добавлена!")
    except ObjectDoesNotExist:
        print("Такой урок не найден!")
