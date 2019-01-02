"""

All blog entries start with post/
Next is the primary key needed represented as <int:pk> 
In Django we can represent the primary key as pk 

"""
from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name = 'home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name = 'post_detail'),
    path('post/new/', BlogCreateView.as_view(), name = 'post_new' ),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name = 'post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name = 'post_delete')
]
