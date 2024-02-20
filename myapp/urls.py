from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name="index"),
    path('about',about,name="about"),
    path('blog',blog,name="blog"),
    path('shop',shop,name='shop')

]
