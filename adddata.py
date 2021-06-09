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

