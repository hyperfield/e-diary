### Данный проект является учебным.

# Скрипты для управления электронным дневником

Для работы данных скриптов нужен развернутый сайт электронного дневника на движке Django с базой данных с именем файла `schoolbase.sqlite3`.

Для начала необходимо скачать файл `scripts.py`, содержащий в себе весь нужный код для управления электронным дневником. Файл находится в репозитории по адресу https://github.com/hyperfield/e-diary.


## Запуск 

После того как файл был скачан, его необходимо разместить на сервере электронного дневника прямо в корневой каталог (директорию) данного сайта.


## Консоль Python Django

Запустить консоль можно следующей командой: `python manage.py shell`. После запуска консоли можно вводить команды, копируя их их файла `scripts.py`. Выйти из консоли можно с помощью команды `exit()`.

## Импортирование моделей и библиотек

В консоли Python Django для работы скриптов необходимо ввести:

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

## Исправление оценок

1. Должна быть запущена консоль Python Django и импортированы приведенные выше модели и библиотеки.
2. Присвоить ФИО ученика переменной `name`, например: `name = 'Фролов Иван Григорьевич'`.
3. Ввести функцию в консоль из файла `scripts.py`.
4. Запустить функцию `def fix_marks(name)` следующим образом: `fix_marks(name)`


## Удаление жалоб

1. Должна быть запущена консоль Python Django и импортированы приведенные выше модели и библиотеки.
2. Присвоить ФИО ученика переменной `name`, например: `name = 'Фролов Иван Григорьевич'`.
3. Ввести функцию `def remove_chastisements(name)` в консоль из файла `scripts.py`.
4. Запустить функцию следующим образом: `remove_chastisements(name)`.


## Добавление похвалы от учителя

1. Должна быть запущена консоль Python Django и импортированы приведенные выше модели и библиотеки.
2. Присвоить имя ученика переменной `name`, например: `name = 'Фролов Иван Григорьевич'`.
3. Присвоить имя учителя переменной `teacher_name`, например: `teacher_name = "Котов Флорентин"`.
4. Присвоить переменной предмет и класс (год) обучения, например: `subject_name = "Математика"`,
`subject_year = 6`.
5. Присвоить переменной текст похвалы, например: `commendation = "С каждым разом у тебя получается всё лучше!"`.
6. (Не обязательно) Собрать все уроки в переменную списка, например: `lessons = Lesson.objects.filter(subject=subject, teacher=teacher)`
7. (Не обязательно) Выбрать нужную дату урока можно путём просмотра дат из списка уроков, введя в консоли:

    for lesson in lessons:
        print(lesson.date)

8. Присвоить переменной выбранную дату, например: `date = datetime.datetime(2018,4,30)`
   В данном примере указывается дата 30 апреля 2018 года. Теперь можно перезапустить поиск в базе данных следующим образом:
   `lesson = Lesson.objects.get(subject=subject, teacher=teacher, date=date)`, сузив таким образом список уроков до одного
   интересующего урока.

   Другой вариант действий это выбрать необходимый урок из списка уроков по спску уроков и дате. Для этого создана функция
   `def get_lessons(lessons, date)` в `scripts.py`.

9. Ввести функцию `def create_commendation(name, subject_name, subject_year, commendation, teacher_name, date)` в консоль.

10. Запустить функцию: `create_commendation(name, subject_name, subject_year, commendation, teacher_name, date)`.



После запуска соответствующих команд можно зайти на сайт электронного дневника и убедиться, что

    1. Оценки исправлены.
    2. Жалобы исчезли.
    3. Появилась похвала от учителя.
