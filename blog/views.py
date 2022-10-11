#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.
from .models import Post
from django.views.generic import ListView, DetailView

class PostList(ListView):
    model = Post
    ordering = '-pk'
    #최신순으로 정렬하기
    #template_name = 'blog/post_list.html'
class PostDetail(DetailView):
    model = Post

'''
def index(request):
    posts = Post.objects.all().order_by('-pk')
    ###최신순으로 보여주기###

    return render(
        request,
        'blog/post_list.html',
        {
            'posts': posts,
        }
    )
    '''

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )
