from django.conf.urls import url

from prc1 import views
from prc1.models import Post
from prc1.views import post_list

urlpatterns = [
    url(r'^posts/', views.post_list, name='post_list'),
]