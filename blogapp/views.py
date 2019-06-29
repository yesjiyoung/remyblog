from django.shortcuts import render, get_object_or_404, redirect #<이거 추가만 하면됨
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
#from django.shortcuts import render, get_object_or_404

# Create your views here.

def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3) #블로글 글 3개씩 나눠서 볼 수 있는 페이지
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', { 'blogs': blogs, 'posts':posts})


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id ) #get_object_or_404(Class, 검색조건) pk = Primary key

    return render(request, 'detail.html',{'blog' : blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()  
      
    return redirect('/blog/' + str(blog.id)) #request()안에 주소는 작성한 db가 그 주소로 넘어가는 기능임
