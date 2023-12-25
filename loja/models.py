from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50)

    def __str__(self):
        return self.title
    
class Product(models.Model):
    user = models.ForeignKey(User,related_name = 'products',on_delete = models.CASCADE)
    category = models.ForeignKey(Category,related_name = 'products',on_delete = models.CASCADE, null = True,blank = True)
    title = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50)
    description = models.TextField(blank = True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    


