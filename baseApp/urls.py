from django.urls import path, include
from rest_framework import routers
from baseApp import views

# api urls
router = routers.DefaultRouter()
router.register(r'users', views.AppUsersView, 'users')

# get post put delete
urlpatterns = [
    path("api/", include(router.urls))
]