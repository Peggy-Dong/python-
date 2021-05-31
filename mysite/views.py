from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import datetime
def index(request):
    return HttpResponse("<h2>group3</h2>")

def date(request):
    return JsonResponse({'date':datetime.datetime.now()})
# Create your views here.
