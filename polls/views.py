from django.shortcuts import render
from django.http import HttpResponse


def index(req):
    return HttpResponse('''
<p><b>Welcome to polls!</b></p>
<p><a href="/">Go to index!</a></p>''')

