from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Career, Subject, Professor, Schedule, Career_Subject, Professor_Subject_Schedule

# Create your views here.

# view para el indice o la primer pagina


class IndexView(generic.ListView):
    template_name = 'schedules/index.html'
    context_object_name = 'career_list'

    def get_queryset(self):
        return Career.objects.all()

# view para los cursos

#
# class CourseView(generic.DetailView):
#     model = Course
#     template_name = 'unimng/course.html'
