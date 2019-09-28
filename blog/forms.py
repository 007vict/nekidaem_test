from django import forms

from blog.models import Blog

class ReadNews(forms.ModelForm):
    reader_news = forms.BooleanField(label='Read this news?')
    class Meta:
        model = Blog
        fields = ('reader_news',)
