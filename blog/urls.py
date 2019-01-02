"""

All blog entries start with post/
Next is the primary key needed represented as <int:pk> 
In Django we can represent the primary key as pk 

"""
from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name = 'home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name = 'post_detail'),
]
