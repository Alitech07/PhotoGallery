from django.urls import path
from .views import (index,
                    Video,
                    AboutPage, 
                    ContactPage, 
                    PostPhotoDelete, 
                    PostPhotoLike, 
                    PostPhotoUpdateView,  
                    PostPhotoCreateView,
                    PhotoDetail,
                    VideoDetail,
                    PostVideoCreateView,
                    PostVideoLike,
                    postphoto_comment,
                    postvideo_comment
                  )

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
  # Pages urls
  path('',index,name='index'),
  path('videos/',Video,name='videos',),
  path('about/',AboutPage.as_view(),name='about'),
  path('contact/',ContactPage.as_view(),name='contact'),

  # PostPhoto urls
  path('post/new/',PostPhotoCreateView.as_view(),name='post_new'),
  path('post/<int:pk>/',PhotoDetail.as_view(),name='photo-detail'),
  path('post/<int:pk>/edit',PostPhotoUpdateView.as_view(),name='post_edit'),
  path('post/<int:pk>/delete',PostPhotoDelete.as_view(),name='post_delete'),
  path('plike/<int:pk>/',PostPhotoLike,name='postphoto_like'),  
  path('post/<int:pk>/comment/',postphoto_comment,name='comments'),

  # Postvideo urls
  path('postvideo/new',PostVideoCreateView.as_view(),name='videopost_new'),
  path('postvideo/<int:pk>/',VideoDetail.as_view(),name='video_detail'),
  path('vlike/<int:pk>/',PostVideoLike,name='postvideo_like'),
  path('postvideo/<int:pk>/videocomment/',postvideo_comment,name='videocomments'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)