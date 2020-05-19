from django.urls import path,re_path
from . import views
urlpatterns = [
    re_path(r'add_os$', views.add_os),
    re_path(r'show_os$', views.show_os),
]
