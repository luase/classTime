from django.db import models

# Carreras
class Career(models.Model):
    name = models.CharField(max_length=45)
    def __str__(self):
        return self.name

# Materias
class Subject(models.Model):
    name = models.CharField(max_length=60)
    hours_per_week = models.IntegerField()
    keycode = models.CharField(max_length=9)
    def __str__(self):
        return self.name

# Profesores/Maestros
class Professor(models.Model):
    name = models.CharField(max_length=60)

#Horarios
class Schedule(models.Model):
    monday = models.CharField(max_length=30, blank=True)
    tuesday = models.CharField(max_length=30, blank=True)
    wednesday = models.CharField(max_length=30, blank=True)
    thursday = models.CharField(max_length=30, blank=True)
    friday = models.CharField(max_length=30, blank=True)
    saturday = models.CharField(max_length=30, blank=True)
    sunday = models.CharField(max_length=30, blank=True)

# Relacion Carreras y Materias
class Career_Subject(models.Model):
    class Meta:
        unique_together = (('career', 'subject'))
    career =  models.ForeignKey(Career, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return self.career.name + " - " + self.subject.name

# Relacion Profesor - Materia - Horario
class Professor_Subject_Schedule(models.Model):
    class Meta:
        unique_together = (('professor', 'schedule'))
    professor =  models.ForeignKey(Career, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    group = models.CharField(max_length=10)
    def __str__(self):
        return self.subject.name + " - " + self.professor.name + " - " + self.schedule.name
