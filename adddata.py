import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()


from mysite.models import Post


for i in range(10):
	newdata = Post(title = "標題{}".format(i),
		body = "內文{}".format(i))
	newdata.save()