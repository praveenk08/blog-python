from django.shortcuts import render, HttpResponse
from . models import Blog
from django.contrib import messages
# Create your views here.
def blogHome(request):
    allBlog = Blog.objects.all()
    context = {'allBlog' : allBlog}
    return render(request, 'blog/blog_layout=list.html',context)

def blogPost(request,slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog': blog}
    return render(request, 'blog/single.html', context)
    # return HttpResponse(f'heml my blogPost page:{slug}')



