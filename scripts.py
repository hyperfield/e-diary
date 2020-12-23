from datacenter.models import Mark
from datacenter.models import Schoolkid
from datacenter.models import Chastisement
from datacenter.models import Subject
from datacenter.models import Commendation
from datacenter.models import Teacher
import random


schoolkid = Schoolkid.objects.get(full_name__contains='Фролов Иван' +
                                  'Григорьевич')


def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for mark in bad_marks:
        if mark.points <= 3:
            mark.points = random.choice([4, 5])
            mark.save()


classmate = Schoolkid.objects.get(full_name__contains='Голубев Феофан')


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


math_teacher = Teacher.objects.get(full_name__contains="Котов Флорентин")
music_teacher = Teacher.objects.get(full_name__contains="Селезнева Майя"
                                    + "Макаровна")
subject = Subject.objects.get(title__contains="Музыка", year_of_study=6)
commendation = "С каждым разом у тебя получается всё лучше!"


def create_commendation(schoolkid, subject, commendation, teacher, date):
    Commendation.objects.create(teacher=teacher, text=commendation,
                                schoolkid=schoolkid, subject=subject,
                                created=date)
