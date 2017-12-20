from django import forms
from blog.models import post


class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['image','title', 'post_content', ]
