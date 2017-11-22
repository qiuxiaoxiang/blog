from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django import forms
from article.models import User


# Create your views here.

#def home(request):
#    return render(request,'home.html')

def home(request):
    posts = Article.objects.all()
    paginator = Paginator(posts,4)
    page = request.GET.get('page')
    try :
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request,'home.html',{'post_list':post_list})

def detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise  Http404
    return render(request,'post.html',{'post':post})

def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request,'archives.html',{'post_list':post_list,'error':False})

def search_tag(request,tag):
    try:
        post_list = Article.objects.filter(category = tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request,'tag.html',{'post_list':post_list})

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'home.html')
        else:
            post_list = Article.objects.filter(title = s)
            if len(post_list) == 0:
                return render(request,'archives.html',{'post_list':post_list,'error':True})
            else:
                return render(request,'archives.html',{'post_list':post_list,'error':False})
    return redirect('/')

class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=50)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')



def regist(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']

            uf = User.objects.create(username=username,password=password,email=email)
            uf.save()

            return render(request,'home.html',{'userform':userform})

    else:
        userform = UserForm()
    return render(request,'regist.html',{'userform':userform})

def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']

            user = User.objects.filter(username__exact=username,password__exact=password)#注意下划线是两杠，我擦搞了半天还以为是那个地方出错了呢。

            if user:
                return render(request,'home.html',{'userform':userform})
            else:
                return HttpResponse('用户名或密码错误，请重新登录')

    else:
        userform = UserForm()
    return render(request,'login.html',{'userform':userform})