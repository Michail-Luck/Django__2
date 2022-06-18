from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import PostForm

# Create your views here.
def main_view(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/index.html', context={'posts': posts})

def post(request,id):
    post = Post.objects.get(id=id)
    return render(request, 'blogapp/post.html', context={'post': post})

def create_post(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'blogapp/create_post.html', context={'form': form})
    else:
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogapp:index'))
        else:
            return render(request, 'blogapp/create_post.html', context={'form': form})

    return render(request, 'blogapp/create_post.html')