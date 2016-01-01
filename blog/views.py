# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    name = "Toroo"
    html = u"<html><body>Сайн уу %s. ажиллаж байна</body></html> "%name
    return HttpResponse(html)