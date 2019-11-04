from django.shortcuts import render,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import random
from .models import MyUser,Company,PostJob,ApplyJob,Question,Result,Contact
from django.core.mail import send_mail
from django.conf import settings
#from .forms import NewUserForm

def search(request):
	if request.POST["technology"]:
		technology=request.POST["technology"]
		search_post=PostJob.objects.filter(title__contains=technology)
		return render(request,'job/index.html',{'search_post':search_post})
	else:
		showpost=PostJob.objects.all()
		return render(request,'job/index.html',{'showpost':showpost})
def index(request):
	try:
		showpost=PostJob.objects.all()
		
		if request.method=="POST":
			email=request.POST['email']
			password=request.POST['password']
			print(email)
			print(password)
			myuser=MyUser.objects.get(email=email,password=password)
			result=Result.objects.all()
			myresult=None
			for i in result:
				print(i.myuser)
				print(i.result)
				if str(i.myuser)==str(myuser.fname):
					myresult=i.result
			print(myresult)

			# print("Result : ",result)
			if myuser:
				request.session['fname']=myuser.fname
				return render(request,'job/index.html',{'myuser':myuser,'showpost':showpost,'myresult':myresult})
			else:
				return render(request,'job/login.html')
	except:
		print("Exception Called")
	return render(request,'job/index.html',{'showpost':showpost})
def about(request):
	return render(request,'job/about.html')
def blog(request):
	return render(request,'job/blog.html')
def base(request):
	return render(request,'job/base.html')
def contact(request):
	return render(request,'job/contact.html')
def job_post(request):
	return render(request,'job/job-post.html')
def new_post(request):
	return render(request,'job/new-post.html')
def register(request):
	if request.method == "POST":
		fname=request.POST['fname']
		lname=request.POST['lname']
		email=request.POST['email']
		contact=request.POST['contact']
		address=request.POST['address']
		#country=request.POST['country']
		#language=request.POST['language']
		#sex=request.POST['sex']
		password=request.POST['password']
		cpassword=request.POST['cpassword']
		
		try:
			myuser=MyUser.objects.get(email=email)
			if myuser:
				msg="Email Already Exist"
				return render(request,'job/job-post.html',{'msg':msg})
		except:
			if password==cpassword:
				MyUser.objects.create(fname=fname,lname=lname,email=email,address=address,contact=contact,password=password,cpassword=cpassword)
				rec=[email,]
				subject="OTP To Complete The Registration"
				otp=random.randint(1000,9999)
				message="Your OTP For Registration Is : "+str(otp)
				email_from = settings.EMAIL_HOST_USER
				send_mail( subject, message, email_from, rec)
				return render(request,'job/otp.html',{'otp':otp})
			else:
				return render(request,'job/job-post.html')	
	else:
		return render(request,'job/job-post.html')
def logout(request):
	showpost=PostJob.objects.all()
	# del request.session['fname']
	return render(request,'job/index.html',{'showpost':showpost})
def logout_company(request):
	return render(request,'job/index.html')
def login(request):
	return render(request,'job/login.html')
def otp(request):
	print(request.POST["g_otp"])
	print(request.POST["e_otp"])
	if request.POST["g_otp"]==request.POST["e_otp"]:
		return render(request,'job/login.html')
	else:
		return render(request,'job/otp.html')
def login_company(request):
	return render(request,'job/login_company.html')
def otp_company(request):
	print(request.POST["g_otp"])
	print(request.POST["e_otp"])
	if request.POST["g_otp"]==request.POST["e_otp"]:
		return render(request,'job/login_company.html')
	else:
		return render(request,'job/otp_company.html')
def register_company(request):
	if request.method == "POST":
		cname=request.POST['cname']
		email=request.POST['email']
		contact=request.POST['contact']
		location=request.POST['location']
		comments=request.POST['comments']
		password=request.POST['password']
		cpassword=request.POST['cpassword']
		if password==cpassword:
			Company.objects.create(cname=cname,email=email,contact=contact,location=location,comments=comments,password=password,cpassword=cpassword)
			rec=[email,]
			subject="OTP To Complete The Registration"
			otp=random.randint(1000,9999)
			message="Your OTP For Registration Is : "+str(otp)
			email_from = settings.EMAIL_HOST_USER
			send_mail( subject, message, email_from, rec)
			return render(request,'job/otp_company.html',{'otp_company':otp_company})
		else:
			return render(request,'job/new-post.html')	
	else:
		return render(request,'job/new-post.html')
def company_index(request):
	try:
		applyjobs=ApplyJob.objects.all()
		print(applyjobs)
		if request.method=="POST":
			email=request.POST['email']
			password=request.POST['password']
			print(email)
			print(password)
			company=Company.objects.get(email=email,password=password)
			if company:
				request.session["email"]=email
				request.session['cname']=company.cname
				return render(request,'job/company_index.html',{'company':company,'applyjobs':applyjobs})
			else:
				return render(request,'job/company_index.html')
	except:
		print("exception caalled")
	return render(request,'job/company_index.html',{'company':company,'applyjobs':applyjobs})
def post_job(request,pk):
	company=get_object_or_404(Company,pk=pk)
	return render(request,'job/post_job.html',{'company':company})

def view_job(request,pk):
	company=get_object_or_404(Company,pk=pk)
	jobview=PostJob.objects.filter(company_name=company.cname)
	print(jobview)
	return render(request, 'job/view-job.html',{'jobview': jobview,'company':company})

def show_candidate(request):
	applyjob=ApplyJob.objects.all()
	print(applyjob)
	return render(request,'job/company_index.html',{'applyjob': applyjob})

def show_job(request):
	showpost=PostJob.objects.all()
	print(showpost)
	return render(request,'job/index.html',{'showpost': showpost})

def view_candidate(request,pk):
	company=get_object_or_404(Company,pk=pk)
	postjobs=PostJob.objects.get(comp=company)

	print("Post Jobs : ",postjobs.title)
	print("Company Name : ",company.cname)
	applyjob=ApplyJob.objects.filter(comp=company)
	print(applyjob[0].myuser)
	result=Result.objects.filter(myuser=applyjob[0].myuser)
	myresult=result[0].result
	myuser=MyUser.objects.get(fname=applyjob[0].myuser)
	print(myuser.resume)
	return render(request, 'job/view_candidate.html',{'applyjob': applyjob,'company':company,'myresult':myresult,'myuser':myuser})

def add_job(request,pk):
	if request.method == "POST":
		company=get_object_or_404(Company,pk=pk)
		print("Company.....",company.cname)
		title=request.POST['title']
		description=request.POST['description']
		Type=request.POST['Type']
		location=request.POST['location']
		category=request.POST['category']
		experiance=request.POST['experiance']
		salary=request.POST['salary']
		vacancies=request.POST['vacancies']
		last_date=request.POST['last_date']
		company_name=request.POST['cname']
		company_description=request.POST['cdescription']
		website=request.POST['company_website']
		PostJob.objects.create(comp=company,title=title,description=description,Type=Type,location=location,category=category,experiance=experiance,salary=salary,vacancies=vacancies,last_date=last_date,company_name=company_name,company_description=company_description,website=website)
		return render(request,'job/company_index.html',{'company':company})
	else:
		return render(request,'job/post_job.html')

def post_edit(request,pk):
	print("PK : ..................",pk)
	job=get_object_or_404(PostJob,pk=pk)
	return render(request,'job/edit_job.html',{'job':job})

def edit_job_done(request,pk):
	if request.method == "POST":
		job=get_object_or_404(PostJob,pk=pk)
		job.title=request.POST['title']
		job.description=request.POST['description']
		job.Type=request.POST['Type']
		job.location=request.POST['location']
		job.category=request.POST['category']
		job.experiance=request.POST['experiance']
		job.salary=request.POST['salary']
		job.vacancies=request.POST['vacancies']
		job.last_date=request.POST['last_date']
		job.company_name=request.POST['company_name']
		job.company_description=request.POST['company_description']
		job.website=request.POST['website']
		job.save()
		return render(request,'job/company_index.html')
	else:
		return render(request,'job/post_job.html')

def delete_job(request,pk,pk1):
	job=get_object_or_404(PostJob,pk=pk)
	job.delete()
	company=get_object_or_404(Company,pk=pk1)
	jobview=PostJob.objects.filter(company_name=company.cname)
	print(jobview)
	return render(request, 'job/view-job.html',{'jobview': jobview,'company':company})

def apply_job(request):
	showpost=PostJob.objects.all()
	return render(request,'job/index.html',{'showpost':showpost})

def apply(request,pk1,pk2):
	print(pk1)
	print(pk2)
	job=get_object_or_404(PostJob,pk=pk1)
	print("Type : ",type(job.title))
	myuser=get_object_or_404(MyUser,pk=pk2)
	result=get_object_or_404(Result,myuser=myuser)
	print("Result : ",result)
	myuser=MyUser.objects.get(fname=request.session['fname'])
	showpost=PostJob.objects.all()
	applyjob=None
	msg=None
	try:
		print("Try Called")
		applyjob=ApplyJob.objects.get(job=job,myuser=myuser)
		print("Type : ",type(applyjob.job))
		print("Apply...............",applyjob.job)
		msg="Applied"
		return render(request,'job/index.html',{'showpost':showpost,'myuser':myuser,'applyjob':applyjob,'msg':msg})
	except:

		print("Exception Called")
		ApplyJob.objects.create(job=job,myuser=myuser,comp=job.comp,result=result)
		msg="Apply"
		return render(request,'job/index.html',{'showpost':showpost,'myuser':myuser,'applyjob':applyjob,'msg':msg})	

def result(request,pk):
	
	myuser=get_object_or_404(MyUser,pk=pk)
	global marks
	marks=0
	try:
		if request.POST['question1']=="rem = fmod(3.14, 2.1);":
			marks=marks+1
	except:
		pass
	try:
		if request.POST['question2']=="AT & T's Bell Laboratories of USA in 1972":
			marks=marks+1
	except:
		pass
	try:
		if request.POST['question3']=="A compiler":
			marks=marks+1
	except:
		pass
	try:
		if request.POST['question4']=="The program may crash if some important data gets ":
			marks=marks+1
	except:
		pass
	try:
		if request.POST['question5']=="constant":
			marks=marks+1
	except:
		pass
	try:
		if request.POST['question6']=="prints the error message specified by the compile":
			marks=marks+1
	except:
		pass
	
	try:
		if request.POST['question7']=="Constant":
			marks=marks+1
	except:
		pass
	try:
		if request.POST['question8']=="7 6":
			marks=marks+1
	except:
		pass
	try:
		if request.POST['question9']=="7":
			marks=marks+1
	except:
		pass
	try:
		if request.POST['question10']=="200":
			marks=marks+1
	except:
		pass
	Result.objects.create(myuser=myuser,result=marks)
	print(marks)
	showpost=PostJob.objects.all()
	applyjob=ApplyJob.objects.all()
	print(applyjob)
	return render(request,'job/index.html',{'showpost':showpost,'myuser':myuser,'applyjob':applyjob})	

def mcq(request,pk):
	myuser=get_object_or_404(MyUser,pk=pk)
	questions=Question.objects.all()
	return render(request,'job/mcq.html',{'questions':questions,'myuser':myuser})

def contact(request):
	if request.method == "POST":
		name=request.POST['name']
		contact_email=request.POST['contact_email']
		subject=request.POST['subject']
		message=request.POST['message']
		Contact.objects.create(name=name,contact_email=contact_email,subject=subject,message=message)
		return render(request,'job/contact.html')
	else:
		return render(request,'job/contact.html')

def company_details(request,pk):
	job=get_object_or_404(PostJob,pk=pk)
	showpost=PostJob.objects.all()
	#applyjob=ApplyJob.objects.all()
	if request.method=="POST":
		email=request.POST['email']
		password=request.POST['password']
		print(email)
		print(password)
		myuser=MyUser.objects.get(email=email,password=password)
		if myuser:
			request.session['fname']=myuser.fname
			return render(request,'job/index.html',{'myuser':myuser,'showpost':showpost})
		else:
			return render(request,'job/login.html')
	return render(request,'job/company_details.html',{'job':job})
