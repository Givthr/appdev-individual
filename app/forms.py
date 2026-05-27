from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 3:
            raise forms.ValidationError("Comment must be at least 3 characters long.")
        return text