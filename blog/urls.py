from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^(?P<blog_id>[0-9]+)/$',views.detail),
    url(r'^(?P<category_type>\w+)/$',views.category)
]