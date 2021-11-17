from django.urls import path

from .views import PostCreateView, PostDeleteView, PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
    path('create/', PostCreateView.as_view(), name='posts_create'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='posts_delete')
]
