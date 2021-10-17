from django.db import models 
from django.contrib.auth.models import User 
from  datetime import datetime

# Create your models here.
class Blog(models.Model): 
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    Img = models.ImageField(upload_to='images/',blank=True,null=True)
    date_time = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self) :
        return self.title

class Contact(models.Model): 
    first_name = models.CharField(max_length=10,null=False)
    last_name = models.CharField(max_length=10,null=False)
    email = models.EmailField(null=False)
    phone = models.IntegerField(null=False)
    message = models.TextField(null=True)
    def __str__(self) :
        return self.email