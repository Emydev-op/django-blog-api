from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('blogs/', views.BlogListView.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', views.BlogDetailsView.as_view(), name='blog-details'),
    # path('comments/', views.CommentListView.as_view(), name='comment-list'),
    # path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
    
    path('blogs/<int:pk>/comments/', views.CommentListView.as_view(), name='comment-list'),
    path('blogs/comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)