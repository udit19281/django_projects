from django.shortcuts import render
import datetime as d
# Create your views here.

def index(response):
    now=d.datetime.now()
    return render(response, 'birthday/index.html',{
        "birthday":  now.day==11 and now.month==3,
        "day": now.day,
        "month": now.month
    })