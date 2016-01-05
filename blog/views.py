# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from blog.models import Blog
from forms import BlogForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

def blogs(request):
    language = 'eng-gb'
    session_language = 'en-gb'
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
        
    if 'lang' in request.session:
        session_language = request.session['lang']
        
    return render_to_response('blogs.html',
    {'blogs':Blog.objects.all(),
     'language':language,
     'session_language':session_language})
     
def blog(request, blog_id=1):
    return render_to_response('blog.html',
    {'blog':Blog.objects.get(id=blog_id)})

def language(request, language='en-gb'):
    response = HttpResponse("setting language to %s" % language)
    response.set_cookie('lang',language)
    request.session['lang'] = language
    return response
    
    
def create(request):
    if request.POST:
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blogs/all')
        else:
            form = BlogForm()
    
        args = {}
        args.update(csrf(request))
        args['form'] = form
        
        return render_to_response('create_blog.html', args)
    
    