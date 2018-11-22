from django.db import models

class Career(models.Model):
    career_name = models.CharField(max_length=30)
    def __str__(self):
        return self.career_name

class Subject(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=60)
    hours_per_week = models.IntegerField(default=0)
    keycode = models.CharField(max_length=9, default="")
    prerequisite = models.CharField(max_length=120, default="")
    group = models.CharField(max_length=5, default="")
    monday = models.CharField(max_length=11, default="")
    tuesday = models.CharField(max_length=11, default="")
    wednesday = models.CharField(max_length=11, default="")
    thursday = models.CharField(max_length=11, default="")
    friday = models.CharField(max_length=11, default="")
    saturday = models.CharField(max_length=11, default="")
    sunday = models.CharField(max_length=11, default="")

    def __str__(self):
        return self.subject_name
