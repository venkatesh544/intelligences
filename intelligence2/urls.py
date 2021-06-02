from django.urls import path

from intelligence2 import views
app_name='intelligence2'

urlpatterns = [
    path('home', views.home, name='home'),
    path('python', views.python, name='python'),
    path('java', views.java, name='java'),
    path('save', views.save, name='save'),
    path('intel', views.intel, name='intel'),

]