from django import forms

from .models import Post

# Add a post form with fields: title and content.
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {
            "title",
            "content",
        }
