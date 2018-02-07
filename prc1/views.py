from datetime import timezone

from django.shortcuts import render, redirect

# Create your views here.
from prc1.forms import PostForm
from prc1.models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts':posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_new')
        else:
            form = PostForm()
        return render(request, 'post_list.html', {'form':form})