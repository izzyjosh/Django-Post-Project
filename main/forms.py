from django import forms
from .models import *

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ("post_body", )
		
		
class UpdateProfile(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ("phone_number", "date_of_birth", )
	class Meta:
		model = User
		fields = ("first_name", "last_name", )
	class Meta:
		models = Image
		fields = ("image", )
	