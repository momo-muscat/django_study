from django.urls import path
from .views import ModelTestView
 
urlpatterns = [
    path("", ModelTestView, name="index"), 
]