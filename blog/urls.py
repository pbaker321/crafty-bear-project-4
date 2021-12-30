from django.urls import path
#from . import views
from .views import BlogView

urlpatterns = [
    #path('', views.blog, name='blog'),
    path('', BlogView.as_view(), name='blog'),
]