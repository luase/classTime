import pandas as pd
from schedules.models import Professor, Subject, Schedule, Career_Subject
from schedules.models import Career, Professor_Subject_Schedule

# correr en la shell de python

# para importar los datos de los profesores:

tmp_data = pd.read_csv('Horarios/professors/p.csv', header=[0], sep=',')

professors = [
    Professor(
        name=row['Name']
    )
    for index, row in tmp_data.iterrows()
]
Professor.objects.bulk_create(professors)

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

tmp_sistemas = pd.read_csv(
    'Horarios/subjects/s_slisc.csv', header=[0], sep=',')
tmp_artes = pd.read_csv('Horarios/subjects/s_slad.csv', header=[0], sep=',')
carreras = Career.objects.all()
materias = Subject.objects.all()

# Bloque de Career_Subject

for index in materias:
    for i in range(0, len(tmp_sistemas)):
        if str(index) == str(tmp_sistemas.iloc[i]['Name']):
            a = [Career_Subject(career=carreras[0], subject=index)]
            Career_Subject.objects.bulk_create(a)

for index in materias:
    for i in range(0, len(tmp_artes)):
        if str(index) == str(tmp_artes.iloc[i]['Name']):
            a = [Career_Subject(career=carreras[1], subject=index)]
            Career_Subject.objects.bulk_create(a)

#Professor_Subject_Schedule Sistemas
cols = ['keycode', 'subject', 'hours_per_week', 'prerequisite', 'group',
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
        'classroom', 'Teacher', 'Career_Lider', 'President' ]

tmp_all_schedules = pd.read_csv('Horarios/career_schedules/dicisHORARIO_2018_2sem_SLISC.csv',
                                header=None, sep=',', names=cols)
profesores = Professor.objects.all()
materias = Subject.objects.all()
horarios = Schedule.objects.all()

temp_professor = profesores[1]
temp_schedule = horarios[1]
temp_subject = materias[1]

for i in range(0, len(tmp_all_schedules)):
    for index in profesores:
        if str(index) == str(tmp_all_schedules.iloc[i]['Teacher']):
            temp_professor = index
            break
    for index2 in materias:
        if str(index2) == str(tmp_all_schedules.iloc[i]['subject']):
            temp_subject = index2
            break
    for index3 in horarios:
         if str(index3.monday) == str(tmp_all_schedules.iloc[i]['Monday']):
            if str(index3.tuesday) == str(tmp_all_schedules.iloc[i]['Tuesday']):
                if str(index3.wednesday) == str(tmp_all_schedules.iloc[i]['Wednesday']):
                    if str(index3.thursday) == str(tmp_all_schedules.iloc[i]['Thursday']):
                        if str(index3.friday) == str(tmp_all_schedules.iloc[i]['Friday']):
                            if str(index3.saturday) == str(tmp_all_schedules.iloc[i]['Saturday']):
                                temp_schedule = index3
                                break
    #print(str(tmp_all_schedules.iloc[i]['Teacher']),' ',str(temp_professor))
    #print(str(tmp_all_schedules.iloc[i]['subject']),' ',str(temp_subject))
    #print(str(tmp_all_schedules.iloc[i]['Monday']),str(tmp_all_schedules.iloc[i]['Tuesday']),str(tmp_all_schedules.iloc[i]['Wednesday']),str(tmp_all_schedules.iloc[i]['Thursday']),str(tmp_all_schedules.iloc[i]['Friday']),str(tmp_all_schedules.iloc[i]['Saturday']),' ',str(temp_schedule))
    a = [Professor_Subject_Schedule(professor = temp_professor,
                                    subject = temp_subject,
                                    schedule = temp_schedule,
                                    group = str(tmp_all_schedules.iloc[i]['group']),
                                    classroom = str(tmp_all_schedules.iloc[i]['classroom']))]
    Professor_Subject_Schedule.objects.bulk_create(a)
#Professor_Subject_Schedule Artes
cols = ['keycode', 'subject', 'hours_per_week', 'prerequisite', 'group',
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
        'classroom', 'Teacher', 'Career_Lider', 'President' ]


tmp_all_schedules = pd.read_csv('Horarios/career_schedules/dicisHORARIO_2018_2sem_SLAD.csv',
                                header=None, sep=',', names=cols)
profesores = Professor.objects.all()
materias = Subject.objects.all()
horarios = Schedule.objects.all()

temp_professor = profesores[1]
temp_schedule = horarios[1]
temp_subject = materias[1]

for i in range(0, len(tmp_all_schedules)):
    for index in profesores:
        if str(index) == str(tmp_all_schedules.iloc[i]['Teacher']):
            temp_professor = index
            break
    for index2 in materias:
        if str(index2) == str(tmp_all_schedules.iloc[i]['subject']):
            temp_subject = index2
            break
    for index3 in horarios:
         if str(index3.monday) == str(tmp_all_schedules.iloc[i]['Monday']):
            if str(index3.tuesday) == str(tmp_all_schedules.iloc[i]['Tuesday']):
                if str(index3.wednesday) == str(tmp_all_schedules.iloc[i]['Wednesday']):
                    if str(index3.thursday) == str(tmp_all_schedules.iloc[i]['Thursday']):
                        if str(index3.friday) == str(tmp_all_schedules.iloc[i]['Friday']):
                            if str(index3.saturday) == str(tmp_all_schedules.iloc[i]['Saturday']):
                                temp_schedule = index3
                                break
    #print(str(tmp_all_schedules.iloc[i]['Teacher']),' ',str(temp_professor))
    #print(str(tmp_all_schedules.iloc[i]['subject']),' ',str(temp_subject))
    #print(str(tmp_all_schedules.iloc[i]['Monday']),str(tmp_all_schedules.iloc[i]['Tuesday']),str(tmp_all_schedules.iloc[i]['Wednesday']),str(tmp_all_schedules.iloc[i]['Thursday']),str(tmp_all_schedules.iloc[i]['Friday']),str(tmp_all_schedules.iloc[i]['Saturday']),' ',str(temp_schedule))
    a = [Professor_Subject_Schedule(professor = temp_professor,
                                    subject = temp_subject,
                                    schedule = temp_schedule,
                                    group = str(tmp_all_schedules.iloc[i]['group']),
                                    classroom = str(tmp_all_schedules.iloc[i]['classroom']))]
    Professor_Subject_Schedule.objects.bulk_create(a)
