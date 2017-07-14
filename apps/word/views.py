# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import strftime, localtime
from django.utils.crypto import get_random_string



def index(request):
    
    if 'counter' not in request.session:
        request.session['counter']=0

    context = {
        "word": get_random_string(length=12)
    }

    request.session['counter'] += 1

    return render(request, 'word/index.html', context)
    

def reset(request):

    request.session.flush()

    return redirect('/')