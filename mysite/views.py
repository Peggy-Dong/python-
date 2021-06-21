from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from mysite.models import Post,Type,Paper,Metal,Plastic,Glass,Textile,Ea,Battery,Cs,Drug,Oil,Other
from mysite.models import Post,Type
from mysite.models import Yilan,Keelung,Taipei,Newtaipei,Taoyuan,Hsinchu,Hsinchuc
from mysite.models import Miaoli,Taichung,Changhua,Nantou,Yunlin
from mysite.models import Chiayi,Chiayic,Tainan,Kaohsiung,Pingtung
from mysite.models import Taitung,Hualien,Renjiang,Kinmen,Penghu
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
	types1=Type.objects.filter(地區="宜蘭縣")
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

def yilan(request):
	types=Type.objects.all()
	types1=Type.objects.filter(地區="宜蘭縣")
	return render(request, "Yilan.html", locals())

def keelung(request):
	types=Type.objects.all()
	types2=Type.objects.filter(地區="基隆市")
	return render(request, "keelung.html", locals())

def taipei(request):
	types=Type.objects.all()
	types3=Type.objects.filter(地區="臺北市")
	return render(request, "taipei.html", locals())

def newtaipei(request):
	types=Type.objects.all()
	types4=Type.objects.filter(地區="新北市")
	return render(request, "newtaipei.html", locals())

def taoyuan(request):
	types=Type.objects.all()
	types5=Type.objects.filter(地區="桃園市")
	return render(request, "taoyuan.html", locals())

def hsinchu(request):
	types=Type.objects.all()
	types6=Type.objects.filter(地區="新竹市")
	return render(request, "hsinchu.html", locals())

def hsinchuc(request):
	types=Type.objects.all()
	types7=Type.objects.filter(地區="新竹縣")
	return render(request, "hsinchuc.html", locals())

def miaoli(request):
	types=Type.objects.all()
	types8=Type.objects.filter(地區="苗栗縣")
	return render(request, "miaoli.html", locals())

def taichung(request):
	types=Type.objects.all()
	types9=Type.objects.filter(地區="臺中市")
	return render(request, "taichung.html", locals())

def changhua(request):
	types=Type.objects.all()
	types10=Type.objects.filter(地區="彰化縣")
	return render(request, "changhua.html", locals())

def nantou(request):
	types=Type.objects.all()
	types11=Type.objects.filter(地區="南投縣")
	return render(request, "nantou.html", locals())

def yunlin(request):
	types=Type.objects.all()
	types12=Type.objects.filter(地區="雲林縣")
	return render(request, "yunlin.html", locals())

def chiayi(request):
	types=Type.objects.all()
	types13=Type.objects.filter(地區="嘉義市")
	return render(request, "chiayi.html", locals())

def chiayic(request):
	types=Type.objects.all()
	types14=Type.objects.filter(地區="嘉義縣")
	return render(request, "chiayic.html", locals())

def tainan(request):
	types=Type.objects.all()
	types15=Type.objects.filter(地區="臺南市")
	return render(request, "tainan.html", locals())

def kaohsiung(request):
	types=Type.objects.all()
	types16=Type.objects.filter(地區="高雄市")
	return render(request, "kaohsiung.html", locals())

def pingtung(request):
	types=Type.objects.all()
	types17=Type.objects.filter(地區="屏東縣")
	return render(request, "pingtung.html", locals())

def taitung(request):
	types=Type.objects.all()
	types18=Type.objects.filter(地區="臺東縣")
	return render(request, "taitung.html", locals())

def hualien(request):
	types=Type.objects.all()
	types19=Type.objects.filter(地區="花蓮縣")
	return render(request, "hualien.html", locals())

def penghu(request):
	types=Type.objects.all()
	types20=Type.objects.filter(地區="澎湖縣")
	return render(request, "penghu.html", locals())

def kinmen(request):
	types=Type.objects.all()
	types21=Type.objects.filter(地區="金門縣")
	return render(request, "kinmen.html", locals())

def renjiang(request):
	types=Type.objects.all()
	types22=Type.objects.filter(地區="連江縣")
	return render(request, "renjiang.html", locals())