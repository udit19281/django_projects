from django.urls import path
from . import views

urlpatterns =[
    path("",views.index,name="index"),
    path("udit/",views.udit,name="udit"),
    path("<str:name>",views.greet,name="greet"),
]