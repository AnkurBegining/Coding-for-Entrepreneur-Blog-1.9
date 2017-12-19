from django import forms
from blog.models import post


class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title', 'post_content', ]
