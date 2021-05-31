from django.shortcuts import render
from django.http import HttpResponse

import datetime
def index(request):
	myname = "Recycle Home"

	return render(request, 'index.html', locals())
 