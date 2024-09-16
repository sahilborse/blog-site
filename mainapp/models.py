import uuid
from django.db import models

# Create your models here.
class CreateBlog(models.Model):
    # id = models.UUIDField(
    #     primary_key=True, 
    #     default=uuid.uuid4, 
    #     editable=False, 
    #     unique=True
    # )
    name=models.CharField(max_length=20)
    email=models.EmailField()
    blog=models.TextField()
    image=models.ImageField()
    
    def __str__(self):
        return self.email
    
    
class Blog(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False, 
        unique=True
    )
    title=models.CharField(max_length=50)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    blog=models.TextField()
    image=models.ImageField()
    
    def __str__(self):
        return self.email