# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView


def hello(request):
    name = "Toroo"
    html = u"<html><body>Сайн уу %s. ажиллаж байна</body></html> "%name
    return HttpResponse(html)
    
def hello_template(request):
    name = "Toroo"
    mytemplate = get_template('hello.html')
    html = mytemplate.render(Context({'name' : name}))
    return HttpResponse(html)
    
def hello_template_simple(request):
    name = "Toroo"
    return render_to_response('hello.html', {'name' : name})
    
class HelloTemplate(TemplateView):
    template_name = 'hello_class.html'
    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = 'Toroo'
        return context
    
    
    
    
    