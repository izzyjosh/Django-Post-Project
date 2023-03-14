from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import re
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Count
from .forms import *

@login_required(login_url="signin")
def index(request):
	
	posts = Post.objects.all().order_by("post_date").reverse()
	comments = Comment.objects.all().annotate(
		num_comment=Count("comment")
		)
	
	context = {
		"posts":posts, 
		"comments":comments, 
	}
	if request.method == "POST":
		comment = request.POST.get("comment")
		
		
	return render(request, "index.html", context)
	

def create_post(request):
	if request.method == "POST":
		post = request.POST.get("post")
		
		Post.objects.create(
			owner = request.user, 
			post_body = post, 
		)
		return redirect("index")
	return render(request, "post.html")


def view_comment(request, post_id):
	post = Post.objects.get(id=post_id)
	
	comments = Comment.objects.filter(post_owner=post).order_by("comment_date").reverse()
	
	if request.method == "POST":
		comment= request.POST.get("comment")
		
		Comment.objects.create(
			comment = comment, 
			post_owner = post, 
			comment_owner = request.user
		)
		return redirect("view_comment", post_id=post_id)
	context = {
		"comments":comments, 
		"post":post
	}
	return render(request, "view_comment.html", context)
	
	
def delete(request, post_id):
	post = Post.objects.get(id=post_id)
	post.delete()
	return redirect("index")
	

def confirm_delete(request, post_id):
	post = Post.objects.get(id=post_id)
	return render(request, "confirm.html", {"post":post})
	

def update(request, post_id):
	post = Post.objects.get(id=post_id)
	form = PostForm(request.POST or None, instance=post)
	
	if form.is_valid():
		form.save()
		return redirect("index")
	return render(request, "form.html", {"form":form})

		
def signup(request):
	
	#function to validate password 
	def validate_password(password):
	       regular_expression = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,1000}$"
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
	