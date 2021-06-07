import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group3.settings')
django.setup()


from mysite.models import Post


with open("recycle1.csv", newline="\n", encoding="utf-8") as csvfile:
	rows = csv.reader(csvfile, delimiter=",")
	for row in rows:
		print(row)
		newdata = Post(year =str(row[0]),title =str(row[1]),body =str(row))
		newdata.save()