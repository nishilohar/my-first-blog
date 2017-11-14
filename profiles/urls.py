from django.conf.urls import url
from django.contrib.auth import views as authViews

from . import views

urlpatterns = [
    url(r'^add-new-story/$', views.add_new_story),
    url(r'^signup/$',views.sign_up),
    url(r'^login/$',views.log_in),
]