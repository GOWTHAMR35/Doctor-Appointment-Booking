from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='doctor'),
    path('saveDoctor',views.saveDoctor,name='saveDoctor'),
    path('saveAppointment',views.saveAppointment,name='saveAppointment'),
    path('listAppointment',views.listAppointment,name='listAppointment')
]