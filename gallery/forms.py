from django import forms
from .models.postsphoto import PhotoComment
from .models.postsvideo import VideoComment

class PhotoNewCommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ['comment']

class VideoNewCommentForm(forms.ModelForm):
    class Meta:
        model = VideoComment
        fields = ['videocomment']