from django.db import models
from django.contrib.auth.models import User
import os
#모델만들고>admin에 작성하기
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)#sale, soldout

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/shoppingMall/tag/{self.slug}/'

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
#unique: 동일한 name을 갖는 카테고리를 만들수없다
    #slugField:고유 url을 만들때,
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/shoppingMall/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories'

class Manufacturer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    phoneNumber = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/shoppingMall/manufacturer/{self.slug}/'

    class Meta:
        verbose_name_plural = 'manufacturers'

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(null=True, blank=True)
    head_image = models.ImageField(upload_to='shoppingMall/images/%Y/%m/%d/', blank=True)
    price = models.IntegerField(null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer,  null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)
    delivery_charge = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}::{self.price} :  {self.manufacturer}'

    def get_absolute_url(self):
        return f'/shoppingMall/{self.pk}/'

'''
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1] # a.text =a txt 제일 마지막'''