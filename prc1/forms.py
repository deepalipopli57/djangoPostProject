from django.forms import models

from prc1.models import Post


class PostForm(models.ModelForm):

    class Meta:
        model = Post
        fields = {'title', 'text',}