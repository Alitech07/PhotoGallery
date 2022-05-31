from tokenize import blank_re
from django.urls import reverse
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from .category import Category

class PostPhoto(models.Model):
  photo = models.ImageField(upload_to = 'images/')
  title = models.CharField(max_length=150)
  body = models.TextField(blank=True,null=True)
  date = models.DateTimeField(auto_now_add=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
  author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    blank=True,
    null=True
  )
  like = models.ManyToManyField(get_user_model(),related_name='postphoto_like')
  views = models.ManyToManyField(get_user_model(),related_name='postphoto_view')

  def number_of_likes(self): 
    return self.like.count()
  
  def total_views(self):
    return self.views.count()

  @staticmethod
  def get_all_postphoto():
    return PostPhoto.objects.all()

  @staticmethod
  def get_all_postphoto_by_categoryid(category_id):
    if category_id:
      return PostPhoto.objects.filter(category = category_id)
    else:
      return PostPhoto.objects.all()

  @property
  def number_of_comments(self):
    return PhotoComment.objects.filter(post=self).count()

    
  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('photo-detail',args=[str(self.id)])

class PhotoComment(models.Model):
  post = models.ForeignKey(PostPhoto,on_delete=models.CASCADE,related_name='comments')
  comment = models.CharField(max_length=250,null=True)
  author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True, null=True)

  class Meta:
    ordering = ('-date',)

  def __str__(self):
    return self.comment
    
  def get_absolute_url(self):
    return reverse('photo-detail')