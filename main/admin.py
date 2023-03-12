from django.contrib import admin
from .models import *

class CommentAdmin(admin.ModelAdmin):
	list_display = ("comment_owner", "comment", "comment_date")
	list_filter = ("comment", )
	search_fields = ("comment", )
	
class PostAdmin(admin.ModelAdmin):
	list_display = ("owner", "post_body", "post_date")
	list_filter = ("post_body", )
	search_fields = ("post_body", )
	
admin.site.register(Image)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)