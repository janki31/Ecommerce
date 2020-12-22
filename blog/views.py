from django.shortcuts import render
from .models import BlogPost

# Create your views here.

def index(request):
    posts=BlogPost.objects.all()
    return render(request,'blog/index.html',{'posts':posts})


def blogpost(request,id):
    bplost=BlogPost.objects.filter(post_id=id)
    return render(request,'blog/blogpost.html',{'post':bplost[0]})