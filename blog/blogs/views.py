from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm


def index(request):
    return render(request, 'blogs/index.html')


@login_required
def blogs(request):
    blogs = Blog.objects.order_by('-date_edit')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)


@login_required
def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    context = {'blog': blog}
    return render(request, 'blogs/blog.html', context)


@login_required
def delete_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('blogs:blogs')


@login_required
def edit_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method != 'POST':
        form = BlogForm(instance=blog)
    else:
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id=blog_id)
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)


@login_required
def new_blog(request):
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog_post = form.save(commit=False)
            new_blog_post.owner = request.user
            new_blog_post.save()
            return redirect('blogs:blogs')
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)
