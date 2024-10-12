from django.shortcuts import render,redirect
from . models import *

def index(request):
    data=DoctorDetails.objects.all()
    return render(request,'doctor.html',{'docData':data})
def saveDoctor(request):
    DoctorDetails(doctorName=request.POST['doctorName'],doctorDegree=request.POST['doctorDegree']).save()
    return render(request,'doctor.html')
def saveAppointment(request):
    appointmentDetails(appDate=request.POST['appDate'],appTime=request.POST['appTime'],patName=request.POST['patName']).save()
    return redirect('/')
def listAppointment(request):
    data=appointmentDetails.objects.all()
    return render(request,'doctor.html',{'appData':data})
