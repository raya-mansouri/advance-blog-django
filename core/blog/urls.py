from django.urls import path
from django.views.generic import TemplateView
from .views import *

name = 'blog'

urlpatterns = [
path("", IndexView.as_view(), name="home"),]
