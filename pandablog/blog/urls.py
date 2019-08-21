from .views import (
				PostList,
				PostDetail,
				create_post_view,
				about_view,
				) #CreatePost

from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', PostList.as_view(), name='home'),
	#path('create/', CreatePost.as_view(), name='create_post'),
	path('create/', create_post_view, name='create_post'),
	path('about/', about_view, name='about'),
	path('', include('sendmail.urls')),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('register/', include('django.contrib.auth.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('summernote/', include('django_summernote.urls')),
]


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)