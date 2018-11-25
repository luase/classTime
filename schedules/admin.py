from django.contrib import admin
from .models import Career, Subject, Professor, Schedule, Career_Subject, Professor_Subject_Schedule

# Register your models here.
admin.site.register(Career)
admin.site.register(Subject)
admin.site.register(Professor)
admin.site.register(Schedule)
admin.site.register(Career_Subject)
admin.site.register(Professor_Subject_Schedule)
