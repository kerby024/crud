# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'crud_app/form.html')

def users(request):
    if request.method == 'POST':
        # users.objects.create(
        #     first_name = '',
        #     last_name = '',
        #     email = ''
        # )
        context = {
            'first_name' :request.POST['first_name']
        }
    return render(request, 'crud_app/show.html', context)

# Create your views here.
