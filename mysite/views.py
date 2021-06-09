from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from mysite.models import Post,Type



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
