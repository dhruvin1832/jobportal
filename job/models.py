from django.conf import settings
from django.db import models
from django.utils import timezone


class MyUser(models.Model):
	fname=models.CharField(max_length=200)
	lname=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	address=models.TextField(blank="true")
	contact=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
	cpassword=models.CharField(max_length=200)
	resume=models.FileField(upload_to='file/') 
	def __str__(self):
		return self.fname

class Company(models.Model):
	cname=models.CharField(max_length=200)
	location=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	comments=models.TextField(blank="true")
	contact=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
	cpassword=models.CharField(max_length=200)
	def __str__(self):
		return self.cname

class PostJob(models.Model):
	comp=models.ForeignKey(Company,on_delete=models.CASCADE)
	title = models.CharField(max_length=300)
	description = models.TextField()
	location=models.CharField(max_length=200)
	Type = models.CharField(max_length=10)
	category = models.CharField(max_length=100)
	experiance = models.CharField(max_length=100)
	salary = models.CharField(max_length=100)
	vacancies = models.CharField(max_length=100)
	last_date = models.DateTimeField()
	company_name = models.CharField(max_length=100)
	company_description=models.TextField()
	website = models.CharField(max_length=100, default="")
	created_at = models.DateTimeField(default=timezone.now)
	filled = models.BooleanField(default=False)
	def __str__(self):
		return self.title

class Result(models.Model):
	myuser=models.ForeignKey(MyUser,on_delete=models.CASCADE)
	result=models.CharField(max_length=100,default=0)
	
class ApplyJob(models.Model):
	comp=models.ForeignKey(Company,on_delete=models.CASCADE)
	job=models.ForeignKey(PostJob,on_delete=models.CASCADE)
	myuser=models.ForeignKey(MyUser,on_delete=models.CASCADE)
	result=models.ForeignKey(Result,on_delete=models.CASCADE)
	applied_date=models.DateTimeField(default=timezone.now)
	status=models.CharField(max_length=200,default="No Action")


class Question(models.Model):
    question = models.TextField(max_length=200,default="")
    option1 = models.CharField(max_length=50,default="")
    option2 = models.CharField(max_length=50, default="")
    option3 = models.CharField(max_length=50, default="")
    option4 = models.CharField(max_length=50, default="")
    answer = models.CharField(max_length=50, default="")

class Contact(models.Model):
	name=models.CharField(max_length=50,default="")
	contact_email=models.CharField(max_length=50,default="")
	subject=models.CharField(max_length=50,default="")
	message=models.TextField(max_length=200,default="")
	def __str__(self):
		return self.name

# class ViewJob(models.Model):
# 	title = models.CharField(max_length=300)
# 	location=models.CharField(max_length=200)
# 	Type = models.CharField(max_length=10)
# 	category = models.CharField(max_length=100)
# 	salary = models.CharFirField(max_length=100)
# 	created_at = models.Daeld(max_length=100)
# 	vacancies = models.ChateTimeField(default=timezone.now)
# 	filled = models.BooleanField(default=False)