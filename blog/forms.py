from django.forms.models import modelformset_factory

from blog.models import Blog

ReadNewsFormSet = modelformset_factory(Blog, fields=('reader_news',), extra=0)









