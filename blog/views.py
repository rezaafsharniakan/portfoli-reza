from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def all_blog(request):
    blogs = Blog.objects.order_by('-date')
    return  render(request, 'blogs/all_blog.html',{'blogs':blogs})
def detail(request, blog_id):
    blog = get_object_or_404(Blog , pk=blog_id)
    return render(request, 'blogs/detail.html',{'blog':blog})