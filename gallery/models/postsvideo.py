from django.urls import reverse
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from gallery.models.category import Category


class PostVideo(models.Model):
  video = models.FileField(upload_to='videos/', null=True)
  title = models.CharField(max_length=150)
  description = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,blank=True,null=True)
  like = models.ManyToManyField(get_user_model(),related_name='postvideo_like')
  views = models.ManyToManyField(get_user_model(),related_name='postvideo_view')


  def number_of_likes(self): 
    return self.like.count()
  
  def total_views(self):
    return self.views.count()


  @staticmethod
  def get_all_postvideo():
    return PostVideo.objects.all()

  @staticmethod
  def get_all_postvideo_by_categoryid(category_id):
    if category_id:
      return PostVideo.objects.filter(category = category_id)
    else:
      return PostVideo.objects.all()

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('video_detail',args=[str(self.id)])

class VideoComment(models.Model):
  postvideo = models.ForeignKey(PostVideo,on_delete=models.CASCADE,related_name='videocomments')
  videocomment = models.CharField(max_length=250)
  author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True, null=True)

  class Meta:
    ordering = ('-date',)


  def __str__(self):
    return self.videocomment

  def get_absolute_url(self):
    return reverse('video_detail')