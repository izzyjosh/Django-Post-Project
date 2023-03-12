from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import re
from django.contrib.auth.decorators import login_required


@login_required(login_url="signin")
def index(request):
	return render(request, "index.html")
	

def signup(request):
	
	#function to validate password 
	def validate_password(password):
	       regular_expression = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,20}$"
	       pattern = re.compile(regular_expression)
	       valid = re.search(pattern, password)
	       return valid
	
	if request.method == "POST":
		username = request.POST.get("username")
		email = request.POST.get("email")
		password = request.POST.get("password1")
		confirm_password= request.POST.get("password2")
	      
	      #calling the function to validate the user inputed password 	
		valid_password = validate_password(password)
		
		#authentications
		if not User.objects.filter(username=username).exists():
			if not User.objects.filter(email=email).exists():
				if valid_password:
					if password == confirm_password:
							
						User.objects.create_user(
							username=username,
							email=email, 
							password=password)
						messages.info(request, f"account for {username} successfully created")
						return redirect("signin")
					else:
						messages.error(request, "both password must match")
				else:
						messages.error(request, "password should be a combination of  numbers, alphabets(upper and lower case ) and minimum length should be 8")
			else:
				messages.error(request, "email already exist!!")		
		else:
			messages.error(request, "username already exist!!")
	return render(request, "signup.html")
	
	
def signin(request):
	
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password1")
		
		user = auth.authenticate(username=username, password=password)
		
		if user is not None:
			auth.login(request, user)
			return redirect("index")
		else:
			messages.error(request, "invalid username or password")
			return redirect("signin")
			
	return render(request, "signin.html")
	
	
def logout(request):
	auth.logout(request)
	return redirect("signin")
	