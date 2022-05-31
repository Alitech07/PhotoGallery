from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView,CreateView,DetailView,UpdateView,DeleteView
from gallery.models.category import Category
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from gallery.models.postsphoto import PhotoComment, PostPhoto
from gallery.models.postsvideo import PostVideo, VideoComment
from django.db.models import Q
from django.core.paginator import Paginator

from .forms import PhotoNewCommentForm, VideoNewCommentForm
# Create your views here.


def PostPhotoLike(request, pk):
  post = get_object_or_404(PostPhoto, id=request.POST.get( "postphoto_id"))
  if post.like.filter(id=request.user.id).exists():
    post.like.remove(request.user)
  else:
    post.like.add(request.user)

  return HttpResponseRedirect(reverse('photo-detail', args=[str(pk)]))

def PostVideoLike(request, pk):
  post = get_object_or_404(PostVideo, id=request.POST.get( "postvideo_id"))
  if post.like.filter(id=request.user.id).exists():
    post.like.remove(request.user)
  else:
    post.like.add(request.user)

  return HttpResponseRedirect(reverse('video_detail', args=[str(pk)]))

#commentariya korstish funksiyasi
def postphoto_comment(request, pk):
    post = get_object_or_404(PostPhoto, id=pk)

    # Обрабатывать POST-запросы
    if request.method == 'POST':
        comment_form = PhotoNewCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect(post)
        else:
            return HttpResponse("Содержание формы неверно, пожалуйста, заполните его.")
    # Обрабатывать плохие запросы
    else:
        return HttpResponse("Публиковать комментарии принимаются только запросы POST.")

def postvideo_comment(request, pk):
    postvideo = get_object_or_404(PostVideo, id=pk)

    #  POST-sorovini tekshirish
    if request.method == 'POST':
        videocomment_form = VideoNewCommentForm(request.POST)
        if videocomment_form.is_valid():
            new_comment = videocomment_form.save(commit=False)
            new_comment.postvideo = postvideo
            new_comment.author = request.user
            new_comment.save()
            return redirect(postvideo)
        else:
            return HttpResponse("Содержание формы неверно, пожалуйста, заполните его.")
    # Обрабатывать плохие запросы
    else:
        return HttpResponse("Публиковать комментарии принимаются только запросы POST.")



def index(request):
  postcategory = None
  categories = Category.get_all_category()

  #Paginator tizimi 
  postlist = PostPhoto.get_all_postphoto().order_by('?')
  pages = Paginator(postlist,12)
  page_number = request.GET.get('page')
  
  #Kategoriyalarga ajratish
  categoryID = request.GET.get("category")
  if categoryID:
    postcategory = PostPhoto.get_all_postphoto_by_categoryid(categoryID)
  elif page_number:
    postcategory = pages.get_page(page_number)
  else:
    postcategory = pages.get_page(1)
  
  #Qidiruv tizimi
  search = request.GET.get('search')
  if search:
    postcategory = PostPhoto.get_all_postphoto().filter(Q(title__icontains=search))
   

  context = {}
  context['categories'] = categories
  context['postphoto'] = postcategory
  context['pages'] = pages
  
  return render(request,'index.html', context)


def Video(request):
  postcategory = None
  categories = Category.get_all_category()

  #Paginator tizimi 
  postlist = PostVideo.get_all_postvideo().order_by('?')
  pages = Paginator(postlist,12)
  page_number = request.GET.get('page')

  #Kategoriyalarga ajratish
  categoryID = request.GET.get("category")
  if categoryID:
    postcategory = PostVideo.get_all_postvideo_by_categoryid(categoryID)
  elif page_number:
    postcategory = pages.page(page_number).object_list
  else:
    postcategory = pages.page(1).object_list

  #Qidiruv tizimi
  search = request.GET.get('search')
  if search:
    postcategory = PostVideo.get_all_postvideo().filter(Q(title__icontains=search))
  
  context = {}
  context['categories'] = categories
  context['postvideo'] = postcategory
  context['pages'] = pages

  return render(request,'videos.html', context)

class PhotoDetail(DetailView):
  model = PostPhoto
  template_name = 'photo-detail.html'
  context_object_name = 'post'

  def get_context_data(self,**kwargs):
    data = super().get_context_data(**kwargs)

    #Korishlar soni
    if self.request.user.id:
      self.object.views.add(self.request.user)

    # like lar soni like bosish tizimi
    like_connected = get_object_or_404(PostPhoto, id=self.kwargs['pk'])
    comments = PhotoComment.objects.filter(post=self.kwargs['pk'])
    liked = False
    if like_connected.like.filter(id=self.request.user.id).exists():
      liked = True
    data['number_of_likes'] = like_connected.number_of_likes()
    data['postphoto_is_liked'] = liked
    data['comments'] = comments

    return data


class ContactPage(TemplateView):
  template_name = 'contact.html'

class AboutPage(TemplateView):
  template_name = 'about.html'

class PostPhotoCreateView(LoginRequiredMixin,CreateView):
  model = PostPhoto
  template_name = 'post_new.html'
  fields = ('photo','title','body','category')

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  
class PostVideoCreateView(LoginRequiredMixin,CreateView):
  model = PostVideo
  template_name = 'videopost_new.html'
  fields = ('video','title','description','category')

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)



class PostPhotoUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
  model = PostPhoto
  template_name = 'post_edit.html'
  fields = ('photo','title','body','category')
  login_url = 'login'

  def test_func(self):
    obj = self.get_object()
    return obj.author == self.request.user

class PostPhotoDelete(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
  model = PostPhoto
  template_name = 'post_delete.html'
  success_url = reverse_lazy('index')
  login_url = 'login'

  def test_func(self):
    obj = self.get_object()
    return obj.author == self.request.user



class VideoDetail(DetailView):
  model = PostVideo
  template_name = 'video_detail.html'
  context_object_name = 'postvideo'

  def get_context_data(self,**kwargs):
    datas = super().get_context_data(**kwargs)

    #Korishlar soni
    if self.request.user.id:
      self.object.views.add(self.request.user)

    # like lar soni like bosish tizimi
    likes_connected = get_object_or_404(PostVideo, id=self.kwargs['pk'])
    comments = VideoComment.objects.filter(postvideo=self.kwargs['pk'])
    likeis = False
    if likes_connected.like.filter(id=self.request.user.id).exists():
      likeis = True
    datas['number_of_likes'] = likes_connected.number_of_likes()
    datas['postvideo_is_liked'] = likeis
    datas['comments'] = comments
    return datas


    
    
    
