from django.urls import path
from .views import BlogView, BlogDetail, AddBlog


urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('details/<int:pk>', BlogDetail.as_view(), name='blog_details'),
    path('add_blog/', AddBlog.as_view(), name='add_blog'),
]
