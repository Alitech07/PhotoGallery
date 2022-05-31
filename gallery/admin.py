from django.contrib import admin
from .models.category import Category
from .models.postsphoto import PostPhoto
from .models.postsvideo import PostVideo
from .models.postsphoto import PhotoComment
from .models.postsvideo import VideoComment
# Register your models here.

class PhotoCommentInline(admin.StackedInline):
  model = PhotoComment

class VideoCommentInline(admin.StackedInline):
  model = VideoComment


class PhotoAdmin(admin.ModelAdmin):
  inlines = [
    PhotoCommentInline
  ]
class VideoAdmin(admin.ModelAdmin):
  inlines = [
    VideoCommentInline
  ]

admin.site.register(Category)
admin.site.register(PostPhoto,PhotoAdmin)
admin.site.register(PostVideo,VideoAdmin)
admin.site.register(PhotoComment)
admin.site.register(VideoComment)