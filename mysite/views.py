from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from mysite.models import Post,Type, Paper



def index(request):
	posts= Post.objects.all()
	myname = "Recycle Home"

	return render(request, 'index.html', locals())
 
def show(request, id):
	try:
		target=Post.objects.get(id=id)
	except:
		return redirect("/")
	return render(request, "showpost.html", locals())

def logout(request):
	auth.logout(request)
	return redirect("/")

def aboutus(request):
	
	return render(request, 'aboutus.html', locals())

def detailed(request):
	posts= Post.objects.all()
	return render(request, 'detailed.html', locals())

def rank(request):
	types=Type.objects.all()
	return render(request, "rank.html", locals())

def paper(request):
	papers=Paper.objects.all()
	return render(request, "paper.html", locals())

def metal(request):
	
	return render(request, "metal.html", locals())
def plastic(request):
	
	return render(request, "plastic.html", locals())
def glass(request):
	
	return render(request, "glass.html", locals())
def textile(request):
	
	return render(request, "textile.html", locals())
def EA(request):
	
	return render(request, "EA.html", locals())
def battery(request):
	
	return render(request, "battery.html", locals())
def CS(request):
	
	return render(request, "CS.html", locals())
def drug(request):
	
	return render(request, "drug.html", locals())
def oil(request):
	
	return render(request, "oil.html", locals())
def other(request):
	
	return render(request, "other.html", locals())