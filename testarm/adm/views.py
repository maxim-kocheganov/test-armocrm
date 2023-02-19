from django.shortcuts import render
from django.http import HttpResponseNotFound
from adm.parser.parser import getPostsFromTG

def index(request):
    return render(request,"home.html")

def getPosts(request):
    posts = getPostsFromTG()