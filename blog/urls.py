from django.urls import path

from blog.apps import BlogConfig

from .views import (PostCreateView, PostDeleteView, PostDetailView,
                    PostListView, PostUpdateView)

app_name = BlogConfig.name

urlpatterns = [
    path("blog/list/", PostListView.as_view(), name="blog"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
]
