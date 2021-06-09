from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    year = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

#class Year(models.Model):
#	year = models.CharField(max_length=200)
#	area =models.CharField(max_length=200)
#	def __str__(self):
#		return self.name

class Type(models.Model):
	年度 = models.CharField(max_length=200)
	地區 =models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)



	def __str__(self):
		return self.年度


