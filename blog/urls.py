from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('post/', views.PostViewSet.as_view({'get': 'list'}), name='post_list'),
    path('comment/', views.CommentViewSet.as_view({'get': 'list'}), name='comment_list')
]
