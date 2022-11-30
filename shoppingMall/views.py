from django.shortcuts import render, redirect
from .models import Post, Category, Tag, Manufacturer
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify

class PostList(ListView):
    model = Post
    ordering = '-pk'
class PostDetail(DetailView):
    model = Post
