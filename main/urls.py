from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"), 
	path("signin/", views.signin, name="signin"), 
	path("signup/", views.signup, name="signup"), 
	path("logout/", views.logout, name="logout"), 
	path("post/", views.create_post, name="create_post"),
	path("view_comment/<int:post_id>/", views.view_comment, name="view_comment"), 
	path("delete/<int:post_id>/", views.delete, name="delete"), 
	path("confirm_delete/<int:post_id>/", views.confirm_delete, name="confirm_delete"), 
	path("update/<int:post_id>/", views.update, name="update")
]