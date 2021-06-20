from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from mysite.models import Post,Type,Paper,Paper1,Plastic,Glass,Textile,Ea,Battery,Cs,Drug,Oil,Other



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

def paper1(request):
	paper1s=Paper1.objects.all()
	return render(request, "paper1.html", locals())

def plastic(request):
	plastics=Plastic.objects.all()
	return render(request, "plastic.html", locals())

def glass(request):
	glasss=Glass.objects.all()
	return render(request, "glass.html", locals())

def textile(request):
	textiles=Textile.objects.all()
	return render(request, "textile.html", locals())

def ea(request):
	eas=Ea.objects.all()
	return render(request, "ea.html", locals())

def battery(request):
	batterys=Battery.objects.all()
	return render(request, "battery.html", locals())

def cs(request):
	css=Cs.objects.all()
	return render(request, "cs.html", locals())

def drug(request):
	drugs=Drug.objects.all()
	return render(request, "drug.html", locals())


def oil(request):
	oils=Oil.objects.all()
	return render(request, "oil.html", locals())

def other(request):
	others=Other.objects.all()
	return render(request, "other.html", locals())