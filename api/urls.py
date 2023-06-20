from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path("api/services/", serviceApiView.as_view()),
    path("api/testimonials/", testimonialApiView.as_view()),
    path("api/team/", teamApiView.as_view()),
    path("api/project/", projectApiView.as_view()),
  
]
