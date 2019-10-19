from django.forms.models import modelformset_factory, ModelForm

from blog.models import Blog

ReadNewsFormSet = modelformset_factory(Blog, fields=('reader_news',), extra=0)

class AddPostForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'body')








