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

class Paper(models.Model):
	地區 = models.CharField(max_length=200)
	民國100年 = models.PositiveIntegerField(default=0)
	民國101年 = models.PositiveIntegerField(default=0)
	民國102年 = models.PositiveIntegerField(default=0)
	民國103年 = models.PositiveIntegerField(default=0)
	民國104年 = models.PositiveIntegerField(default=0)
	民國105年 = models.PositiveIntegerField(default=0)
	民國106年 = models.PositiveIntegerField(default=0)
	民國107年 = models.PositiveIntegerField(default=0)
	民國108年 = models.PositiveIntegerField(default=0)
	民國109年 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.地區


class metal(models.Model):
	地區 = models.CharField(max_length=200)
	民國100年 = models.PositiveIntegerField(default=0)
	民國101年 = models.PositiveIntegerField(default=0)
	民國102年 = models.PositiveIntegerField(default=0)
	民國103年 = models.PositiveIntegerField(default=0)
	民國104年 = models.PositiveIntegerField(default=0)
	民國105年 = models.PositiveIntegerField(default=0)
	民國106年 = models.PositiveIntegerField(default=0)
	民國107年 = models.PositiveIntegerField(default=0)
	民國108年 = models.PositiveIntegerField(default=0)
	民國109年 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.地區

class plastic(models.Model):
	地區 = models.CharField(max_length=200)
	民國100年 = models.PositiveIntegerField(default=0)
	民國101年 = models.PositiveIntegerField(default=0)
	民國102年 = models.PositiveIntegerField(default=0)
	民國103年 = models.PositiveIntegerField(default=0)
	民國104年 = models.PositiveIntegerField(default=0)
	民國105年 = models.PositiveIntegerField(default=0)
	民國106年 = models.PositiveIntegerField(default=0)
	民國107年 = models.PositiveIntegerField(default=0)
	民國108年 = models.PositiveIntegerField(default=0)
	民國109年 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.地區

class glass(models.Model):
	地區 = models.CharField(max_length=200)
	民國100年 = models.PositiveIntegerField(default=0)
	民國101年 = models.PositiveIntegerField(default=0)
	民國102年 = models.PositiveIntegerField(default=0)
	民國103年 = models.PositiveIntegerField(default=0)
	民國104年 = models.PositiveIntegerField(default=0)
	民國105年 = models.PositiveIntegerField(default=0)
	民國106年 = models.PositiveIntegerField(default=0)
	民國107年 = models.PositiveIntegerField(default=0)
	民國108年 = models.PositiveIntegerField(default=0)
	民國109年 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.地區
class textile(models.Model):
	地區 = models.CharField(max_length=200)
	民國100年 = models.PositiveIntegerField(default=0)
	民國101年 = models.PositiveIntegerField(default=0)
	民國102年 = models.PositiveIntegerField(default=0)
	民國103年 = models.PositiveIntegerField(default=0)
	民國104年 = models.PositiveIntegerField(default=0)
	民國105年 = models.PositiveIntegerField(default=0)
	民國106年 = models.PositiveIntegerField(default=0)
	民國107年 = models.PositiveIntegerField(default=0)
	民國108年 = models.PositiveIntegerField(default=0)
	民國109年 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.地區
class EA(models.Model):
	地區 = models.CharField(max_length=200)
	民國100年 = models.PositiveIntegerField(default=0)
	民國101年 = models.PositiveIntegerField(default=0)
	民國102年 = models.PositiveIntegerField(default=0)
	民國103年 = models.PositiveIntegerField(default=0)
	民國104年 = models.PositiveIntegerField(default=0)
	民國105年 = models.PositiveIntegerField(default=0)
	民國106年 = models.PositiveIntegerField(default=0)
	民國107年 = models.PositiveIntegerField(default=0)
	民國108年 = models.PositiveIntegerField(default=0)
	民國109年 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.地區

class battery(models.Model):
	地區 = models.CharField(max_length=200)
	民國100年 = models.PositiveIntegerField(default=0)
	民國101年 = models.PositiveIntegerField(default=0)
	民國102年 = models.PositiveIntegerField(default=0)
	民國103年 = models.PositiveIntegerField(default=0)
	民國104年 = models.PositiveIntegerField(default=0)
	民國105年 = models.PositiveIntegerField(default=0)
	民國106年 = models.PositiveIntegerField(default=0)
	民國107年 = models.PositiveIntegerField(default=0)
	民國108年 = models.PositiveIntegerField(default=0)
	民國109年 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.地區

class CS(models.Model):
	地區 = models.CharField(max_length=200)
	民國100年 = models.PositiveIntegerField(default=0)
	民國101年 = models.PositiveIntegerField(default=0)
	民國102年 = models.PositiveIntegerField(default=0)
	民國103年 = models.PositiveIntegerField(default=0)
	民國104年 = models.PositiveIntegerField(default=0)
	民國105年 = models.PositiveIntegerField(default=0)
	民國106年 = models.PositiveIntegerField(default=0)
	民國107年 = models.PositiveIntegerField(default=0)
	民國108年 = models.PositiveIntegerField(default=0)
	民國109年 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.地區

class drug(models.Model):
	地區 = models.CharField(max_length=200)
	民國100年 = models.PositiveIntegerField(default=0)
	民國101年 = models.PositiveIntegerField(default=0)
	民國102年 = models.PositiveIntegerField(default=0)
	民國103年 = models.PositiveIntegerField(default=0)
	民國104年 = models.PositiveIntegerField(default=0)
	民國105年 = models.PositiveIntegerField(default=0)
	民國106年 = models.PositiveIntegerField(default=0)
	民國107年 = models.PositiveIntegerField(default=0)
	民國108年 = models.PositiveIntegerField(default=0)
	民國109年 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.地區

class oil(models.Model):
	地區 = models.CharField(max_length=200)
	民國100年 = models.PositiveIntegerField(default=0)
	民國101年 = models.PositiveIntegerField(default=0)
	民國102年 = models.PositiveIntegerField(default=0)
	民國103年 = models.PositiveIntegerField(default=0)
	民國104年 = models.PositiveIntegerField(default=0)
	民國105年 = models.PositiveIntegerField(default=0)
	民國106年 = models.PositiveIntegerField(default=0)
	民國107年 = models.PositiveIntegerField(default=0)
	民國108年 = models.PositiveIntegerField(default=0)
	民國109年 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.地區

class other(models.Model):
	地區 = models.CharField(max_length=200)
	民國100年 = models.PositiveIntegerField(default=0)
	民國101年 = models.PositiveIntegerField(default=0)
	民國102年 = models.PositiveIntegerField(default=0)
	民國103年 = models.PositiveIntegerField(default=0)
	民國104年 = models.PositiveIntegerField(default=0)
	民國105年 = models.PositiveIntegerField(default=0)
	民國106年 = models.PositiveIntegerField(default=0)
	民國107年 = models.PositiveIntegerField(default=0)
	民國108年 = models.PositiveIntegerField(default=0)
	民國109年 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.地區
