import pandas as pd
from schedules.models import Professor, Subject, Schedule

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
