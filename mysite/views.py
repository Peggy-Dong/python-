from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from mysite.models import Post,Type,Paper,Metal,Plastic,Glass,Textile,Ea,Battery,Cs,Drug,Oil,Other
from mysite.models import Post,Type
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage



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
	post_all= Post.objects.all()

	paginator = Paginator(post_all, 5)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger: 
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request, 'detailed.html', locals())

def rank(request):
	type_all=Type.objects.all()

	tpaginator = Paginator(type_all, 22)
	tpage = request.GET.get('page')
	try:
		types = tpaginator.page(tpage)
	except PageNotAnInteger: 
		types = tpaginator.page(1)
	except EmptyPage:
		types = tpaginator.page(tpaginator.num_pages)
	return render(request, "rank.html", locals())

def paper(request):
	papers=Paper.objects.all()
	return render(request, "paper.html", locals())

def metal(request):
	metals=Metal.objects.all()
	return render(request, "metal.html", locals())

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

def chart(request):
	types=Type.objects.all()
	types1=Type.objects.filter(地區="新北市")
	types100=Type.objects.filter(年度="100年")
	types101=Type.objects.filter(年度="101年")
	types102=Type.objects.filter(年度="102年")
	types103=Type.objects.filter(年度="103年")
	types104=Type.objects.filter(年度="104年")
	types105=Type.objects.filter(年度="105年")
	types106=Type.objects.filter(年度="106年")
	types107=Type.objects.filter(年度="107年")
	types108=Type.objects.filter(年度="108年")
	types109=Type.objects.filter(年度="109年")

	return render(request, "chart.html", locals())
