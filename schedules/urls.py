from django.urls import path

from . import views

app_name = 'schedules'
urlpatterns = [
    # ex: /schedules/
    path('', views.IndexView.as_view(), name='index' )
    #path('', views.index, name='index'),
]
