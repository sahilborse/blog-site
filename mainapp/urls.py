from mainapp import views
from django.urls import path,include

urlpatterns = [
    path('create/',views.create, name='create' ),
    path('', views.index,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('blog/<str:id>/', views.blog_detail, name='blog_detail'),
]
