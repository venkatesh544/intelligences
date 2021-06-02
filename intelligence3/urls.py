from django.urls import path

from intelligence3 import views

urlpatterns = [
    path('bdaloginpage', views.bdaloginpage, name='bdaloginpage')

]