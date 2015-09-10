from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages



# Create your views here.

def login(request):
	args={}
	args.update(csrf(request))
	if request.method == "POST":

		username=request.POST.get('username','')
		password=request.POST.get('password','')
		
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			user = None
		

		if user is not None and (user.password==password):
			user.backend = 'django.contrib.auth.backends.ModelBackend'
			auth.login(request, user)
			return redirect('/')
		elif user is not None:
			args['password_error']="Incorrect password"
			return render_to_response('login.html', args)
		else:
			args['login_error']="User Does Not Exist"			
			return render_to_response('login.html', args)
	else:
		return render_to_response('login.html',args)

def register(request):
	args={}
	args.update(csrf(request))
	if request.method == "POST":

		username=request.POST.get('username','')
		password=request.POST.get('password','')
		email=request.POST.get('email','')

		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			user = None
		
		if user is None:
			user = User.objects.create_user(username, password, email)
			user.password=password
			user.email=email
			user.save()
			user.backend = 'django.contrib.auth.backends.ModelBackend'
			auth.login(request, user)
			return redirect('/')
		else:
			args['login_error']="User is alredy exist"
			return render_to_response('register.html', args)
	
	else:
		return render_to_response('register.html',args)

def recoverlogin(request):
	args={}
	args.update(csrf(request))
	if request.method == "POST":

		username=request.POST.get('username','')
		email=request.POST.get('email','')
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			user = None
		

		if user is not None and (email==user.email):
			send_mail('Password recovery', "Dear "+username+"! Your password:"+user.password+". \n Get Lucky! Please, be more attantive in future! \n Administration.", "boghdanandreev@gmail.com", [email], fail_silently=0)
			return redirect('/')

		elif user is not None:
			args['email_error']="Incorrect email"
			return render_to_response('recover.html', args)
		
		else:
			args['login_error']="User Does Not Exist. Try to "			
			return render_to_response('recover.html', args)
	else:
		return render_to_response('recover.html',args)



def logout(request):
	auth.logout(request)
	return redirect("/")