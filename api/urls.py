from django.contrib import admin
from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', home),
    path("api/services/", serviceApiView.as_view()),
    path("api/testimonials/", testimonialApiView.as_view()),
    path("api/team/", teamApiView.as_view()),
    path("api/project/", projectApiView.as_view()),
    path("api/course/", courseAPIView.as_view()),
    # Endpoint for fetching a specific blog by ID
    path("api/course/<int:course_id>/", courseAPIView.as_view(), name="course-detail"),
    path("api/blog/", blogApiView.as_view()),
    # Endpoint for fetching a specific blog by ID
    path("api/blog/<int:blog_id>/", blogApiView.as_view(), name="blog-detail"),
    path('api/contact/', contact, name='contact'),
    # path('api/contact/', contactApiView.as_view(), name='contact'),
    

  
]
