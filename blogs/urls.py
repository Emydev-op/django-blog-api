from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('blogs/', views.BlogListView.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', views.BlogDetailsView.as_view(), name='blog-details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)