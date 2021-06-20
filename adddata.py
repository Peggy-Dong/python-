import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group3.settings')
django.setup()


from mysite.models import Type

with open("recycle1.csv", newline="\n", encoding="utf-8") as csvfile:
	rows = csv.reader(csvfile, delimiter=",")
	for row in rows:
		print(row)
		newdata = Type(年度 =str(row[0]),地區 =str(row[1]),總計 =str(row[2]),紙類 =str(row[3]),金屬類 =str(row[4]),塑膠橡膠 =str(row[5]),玻璃 =str(row[6]),紡織品 =str(row[7]),家用電品 =str(row[8]),電池 =str(row[9]),通訊物品 =str(row[10]),特殊用藥廢容器 =str(row[11]),食用油 =str(row[12]),其他 =str(row[13]))
		newdata.save()


from mysite.models import Paper

with open("paper.csv", newline="\n", encoding="utf-8") as csvfile:
	rows = csv.reader(csvfile, delimiter=",")
	for row in rows:
		print(row)
		newdata = Paper(地區 =str(row[0]),民國100年 =str(row[1]),民國101年 =str(row[2]),民國102年 =str(row[3]),民國103年 =str(row[4]),民國104年 =str(row[5]),民國105年 =str(row[6]),民國106年 =str(row[7]),民國107年 =str(row[8]),民國108年 =str(row[9]),民國109年 =str(row[10]))
		newdata.save()

from mysite.models import Paper1

with open("m1.csv", newline="\n", encoding="utf-8") as csvfile:
	rows = csv.reader(csvfile, delimiter=",")
	for row in rows:
		print(row)
		newdata = Paper1(地區 =str(row[0]),民國100年 =str(row[1]),民國101年 =str(row[2]),民國102年 =str(row[3]),民國103年 =str(row[4]),民國104年 =str(row[5]),民國105年 =str(row[6]),民國106年 =str(row[7]),民國107年 =str(row[8]),民國108年 =str(row[9]),民國109年 =str(row[10]))
		newdata.save()

from mysite.models import Plastic

with open("plas.csv", newline="\n", encoding="utf-8") as csvfile:
	rows = csv.reader(csvfile, delimiter=",")
	for row in rows:
		print(row)
		newdata = Plastic(地區 =str(row[0]),民國100年 =str(row[1]),民國101年 =str(row[2]),民國102年 =str(row[3]),民國103年 =str(row[4]),民國104年 =str(row[5]),民國105年 =str(row[6]),民國106年 =str(row[7]),民國107年 =str(row[8]),民國108年 =str(row[9]),民國109年 =str(row[10]))
		newdata.save()

from mysite.models import Glass

with open("glas.csv", newline="\n", encoding="utf-8") as csvfile:
	rows = csv.reader(csvfile, delimiter=",")
	for row in rows:
		print(row)
		newdata = Glass(地區 =str(row[0]),民國100年 =str(row[1]),民國101年 =str(row[2]),民國102年 =str(row[3]),民國103年 =str(row[4]),民國104年 =str(row[5]),民國105年 =str(row[6]),民國106年 =str(row[7]),民國107年 =str(row[8]),民國108年 =str(row[9]),民國109年 =str(row[10]))
		newdata.save()


from mysite.models import Textile
with open("tex.csv", newline="\n", encoding="utf-8") as csvfile:
	rows = csv.reader(csvfile, delimiter=",")
	for row in rows:
		print(row)
		newdata = Textile(地區 =str(row[0]),民國100年 =str(row[1]),民國101年 =str(row[2]),民國102年 =str(row[3]),民國103年 =str(row[4]),民國104年 =str(row[5]),民國105年 =str(row[6]),民國106年 =str(row[7]),民國107年 =str(row[8]),民國108年 =str(row[9]),民國109年 =str(row[10]))
		newdata.save()


from mysite.models import Ea
with open("ea1.csv", newline="\n", encoding="utf-8") as csvfile:
	rows = csv.reader(csvfile, delimiter=",")
	for row in rows:
		print(row)
		newdata = Ea(地區 =str(row[0]),民國100年 =str(row[1]),民國101年 =str(row[2]),民國102年 =str(row[3]),民國103年 =str(row[4]),民國104年 =str(row[5]),民國105年 =str(row[6]),民國106年 =str(row[7]),民國107年 =str(row[8]),民國108年 =str(row[9]),民國109年 =str(row[10]))
		newdata.save()


from mysite.models import Battery
with open("bat.csv", newline="\n", encoding="utf-8") as csvfile:
	rows = csv.reader(csvfile, delimiter=",")
	for row in rows:
		print(row)
		newdata = Battery(地區 =str(row[0]),民國100年 =str(row[1]),民國101年 =str(row[2]),民國102年 =str(row[3]),民國103年 =str(row[4]),民國104年 =str(row[5]),民國105年 =str(row[6]),民國106年 =str(row[7]),民國107年 =str(row[8]),民國108年 =str(row[9]),民國109年 =str(row[10]))
		newdata.save()

from mysite.models import Cs
with open("cs.csv", newline="\n", encoding="utf-8") as csvfile:
	rows = csv.reader(csvfile, delimiter=",")
	for row in rows:
		print(row)
		newdata = Cs(地區 =str(row[0]),民國100年 =str(row[1]),民國101年 =str(row[2]),民國102年 =str(row[3]),民國103年 =str(row[4]),民國104年 =str(row[5]),民國105年 =str(row[6]),民國106年 =str(row[7]),民國107年 =str(row[8]),民國108年 =str(row[9]),民國109年 =str(row[10]))
		newdata.save()

from mysite.models import Drug
with open("drug.csv", newline="\n", encoding="utf-8") as csvfile:
	rows = csv.reader(csvfile, delimiter=",")
	for row in rows:
		print(row)
		newdata = Drug(地區 =str(row[0]),民國100年 =str(row[1]),民國101年 =str(row[2]),民國102年 =str(row[3]),民國103年 =str(row[4]),民國104年 =str(row[5]),民國105年 =str(row[6]),民國106年 =str(row[7]),民國107年 =str(row[8]),民國108年 =str(row[9]),民國109年 =str(row[10]))
		newdata.save()


from mysite.models import Oil
with open("oil1.csv", newline="\n", encoding="utf-8") as csvfile:
	rows = csv.reader(csvfile, delimiter=",")
	for row in rows:
		print(row)
		newdata = Oil(地區 =str(row[0]),民國100年 =str(row[1]),民國101年 =str(row[2]),民國102年 =str(row[3]),民國103年 =str(row[4]),民國104年 =str(row[5]),民國105年 =str(row[6]),民國106年 =str(row[7]),民國107年 =str(row[8]),民國108年 =str(row[9]),民國109年 =str(row[10]))
		newdata.save()

from mysite.models import Other
with open("other1.csv", newline="\n", encoding="utf-8") as csvfile:
	rows = csv.reader(csvfile, delimiter=",")
	for row in rows:
		print(row)
		newdata = Other(地區 =str(row[0]),民國100年 =str(row[1]),民國101年 =str(row[2]),民國102年 =str(row[3]),民國103年 =str(row[4]),民國104年 =str(row[5]),民國105年 =str(row[6]),民國106年 =str(row[7]),民國107年 =str(row[8]),民國108年 =str(row[9]),民國109年 =str(row[10]))
		newdata.save()