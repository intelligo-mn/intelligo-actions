from django import forms
from models import Blog

class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ('title', 'body', 'pub_date')