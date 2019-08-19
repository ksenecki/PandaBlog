from .views import PostList, PostDetail, CreatePost
from django.urls import path, include


urlpatterns = [
    path('', PostList.as_view(), name='home'),
	path('create/', CreatePost.as_view(), name='create_post'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('register/', include('django.contrib.auth.urls')),
]