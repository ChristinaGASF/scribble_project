from django.conf.urls import include
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('scribble.urls')),
    path('posts/new', views.post_create, name='post_create'),
    path('posts/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('posts/<int:pk>/delete', views.post_delete, name='post_delete'),
    path('comments/new', views.comment_create, name='comment_create'),
    path('comments/<int:pk>/edit', views.comment_edit, name='comment_edit'),
    path('comments/<int:pk>/delete', views.comment_delete, name='comment_delete'),
]