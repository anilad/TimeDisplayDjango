from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from datetime import datetime

def index(request):
    context = {
        "date": datetime.now().date(),
        "time": datetime.now().time().strftime('%I:%M %p'),  
    }
    return render(request,'timeDisplayApp/index.html', context)
