from django.shortcuts import render

# Create your views here.
tasklist=["foo","bar","baz"]
def index(request):
    return render(request,"tasks/index.html",({
        "tasklist":tasklist
    }))

def add(request):
    return render(request,"tasks/add.html")