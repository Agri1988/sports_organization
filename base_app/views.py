import datetime

from django.shortcuts import render


def index(request):
    return render(request, 'base_app/base.html')
