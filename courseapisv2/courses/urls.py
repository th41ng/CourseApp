
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

r = DefaultRouter();
r.register('categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(r.urls)),

]
