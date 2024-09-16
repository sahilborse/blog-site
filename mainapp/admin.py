from django.contrib import admin
from mainapp.models import CreateBlog
from .models import Blog
# Register your models here.
admin.site.register(CreateBlog)


admin.site.register(Blog)