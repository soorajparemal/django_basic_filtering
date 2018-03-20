
from django.conf.urls import url, include
from django.contrib import admin
from .views import home,listall



urlpatterns = [

    url(r'^$', home),
    url(r'^listall/', listall),

]