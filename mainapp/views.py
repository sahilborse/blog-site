from django.shortcuts import render, get_object_or_404
from mainapp.models import CreateBlog
from mainapp.models import Blog
from django.contrib import messages

# Create your views here.
def index(request):
    mydata = Blog.objects.all().values()
    context = {
        'mymembers': mydata,
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('title')
        image = request.POST.get('image')
        blog = request.POST.get('blog')
    
        createBlog = Blog(name=name, email=email,title=title,image=image, blog=blog)
        createBlog.save()
        messages.success(request, "Data has been saved successfully.")
    
    return render(request, 'create.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog_detail(request,id):
    blog = get_object_or_404(Blog, title=id)
   
    context = {
        'blog': blog
    }
    return render(request, 'blog_detail.html', context)