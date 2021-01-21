from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='content', max_length = 500)
    class Meta:
        model = Comment
        fields = ['content']