from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="user_image")
	
	def __str__(self):
		return self.user
		
class Post(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	post_body = models.TextField()
	post_date= models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.post_body
		
class Comment(models.Model):
	post_owner = models.ForeignKey(Post, on_delete=models.CASCADE)
	comment_owner = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.CharField(max_length=100)
	comment_date = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.comment