from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Career

class IndexView(generic.ListView):
    template_name = 'schedules/index.html'
    context_object_name = 'careers_list'
    def get_queryset(self):
        return Career.objects.all()
"""
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
"""
