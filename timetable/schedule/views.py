from django.shortcuts import render
from .models import ClassSchedule

def index(request):
    schedules = ClassSchedule.objects.all()
    return render(request, 'schedule/index.html', {'schedules': schedules})
