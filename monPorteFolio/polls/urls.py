from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    re_path(r'^projets$',views.projets,name="projets"),
    re_path(r'^contact',views.contact,name="contact")
]
