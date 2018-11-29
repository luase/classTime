import pandas as pd
from schedules.models import Professor, Subject, Schedule, Career_Subject
from schedules.models import Career, Professor_Subject_Schedule
import sys

# correr en la shell de python

# para importar los datos de los profesores:

tmp_data = pd.read_csv('Horarios/professors/p.csv', header=[0], sep=',')

professors = [
    Professor(
        name=row['Name']
    )
    for index, row in tmp_data.iterrows()
]
Profesor.objects.bulk_create(professors)

# para importar los datos de las materias

tmp_data = pd.read_csv('Horarios/subjects/s.csv', header=[0], sep=',')

subjects = [
    Subject(
        name=row['Name'],
        hours_per_week=row['Hours At Week'],
        keycode=row['Keycode']
    )
    for index, row in tmp_data.iterrows()
]
Subject.objects.bulk_create(subjects)

# para importar los datos de los horarios

tmp_data = pd.read_csv('Horarios/schedules/sch.csv', header=[0], sep=',')

schedules = [
    Schedule(
        monday=row['Monday'],
        tuesday=row['Tuesday'],
        wednesday=row['Wednesday'],
        thursday=row['Thursday'],
        friday=row['Friday'],
        saturday=row['Saturday']
    )
    for index, row in tmp_data.iterrows()
]
Schedule.objects.bulk_create(schedules)

# Bloque de Career_Subject

tmp_sistemas = pd.read_csv('Horarios/subjects/s_slisc.csv', header=[0], sep=',')
tmp_artes = pd.read_csv('Horarios/subjects/s_slad.csv', header=[0], sep=',')
carreras = Career.objects.all()
materias = Subject.objects.all()

# Bloque de Career_Subject

for index in materias:
    for i in range(0, len(tmp_sistemas)):
        if str(index) == str(tmp_sistemas.iloc[i]['Name']):
            a = [Career_Subject(career = carreras[1],subject = index)]
            Career_Subject.objects.bulk_create(a)

for index in materias:
    for i in range(0, len(tmp_artes)):
        if str(index) == str(tmp_artes.iloc[i]['Name']):
            a = [Career_Subject(career = carreras[0],subject = index)]
            Career_Subject.objects.bulk_create(a)

# Bloque de Professor_Subject_Schedule

cols = ['keycode', 'subject', 'hours_per_week', 'prerequisite', 'group',
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
        'classroom', 'Teacher', 'Career_Lider', 'President' ]

tmp_all_schedules = pd.read_csv('Horarios/career_schedules/dicisHORARIOS.csv',
                                header=None, sep=',', names=cols)

profesores = Professor.objects.all()
materias = Subject.objects.all()
horarios = Schedule.objects.all()

for index in profesores:
    for index2 in materias:
        for index3 in horarios:
            for i in range(0, len(tmp_all_schedules)):
                Mo = str(tmp_all_schedules.iloc[i]['Monday'])
                Tu = str(tmp_all_schedules.iloc[i]['Tuesday'])
                We = str(tmp_all_schedules.iloc[i]['Wednesday'])
                Th = str(tmp_all_schedules.iloc[i]['Thursday'])
                Fr = str(tmp_all_schedules.iloc[i]['Friday'])
                Sa = str(tmp_all_schedules.iloc[i]['Saturday'])
                Sc = [ Mo, Tu, We, Th, Fr, Sa ]
                if ( str(index) == str(tmp_all_schedules.iloc[i]['Teacher']) and
                    str(index2) == str(tmp_all_schedules.iloc[i]['subject']) and
                    str(index3) == Sc ):
                    a = [Professor_Subject_Schedule(professor = index,
                                                    subject = index2,
                                                    schedule = index3,
                                                    group = str(tmp_all_schedules.iloc[i]['group']),
                                                    classroom = str(tmp_all_schedules.iloc[i]['classroom']))]
                    Professor_Subject_Schedule.objects.bulk_create(a)
