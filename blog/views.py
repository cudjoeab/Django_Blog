from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from blog.models import Article, Comment

def root(request):
    return HttpResponseRedirect('/home')

def home_page(request):
    # context = {}

    context = { 
    'articles': Article.objects.all().order_by('-published_date'),
    'current_time': datetime.now() 
    }
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def blog_show(request, id):
    article = Article.objects.get(pk=id)
    context = {'article': article }
    response = render(request, 'show.html', context)
    return HttpResponse(response)

def create_comment(request):
    article_id = request.POST['article']
    article = Article.objects.get(id=article_id)
    new_comment = Comment()
    new_comment.name = request.POST['name']
    new_comment.message = request.POST['message']
    new_comment.article = article
    new_comment.save()
    context = {'article': article}
    response = render(request, 'show.html', context)
    return HttpResponse(response) 