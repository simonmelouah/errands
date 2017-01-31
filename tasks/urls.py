from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.sign_in, name='sign_in'),
    url(r'^$sign_in', views.sign_in, name='sign_in'),
    url(r'^index/$', views.index, name='index'),
    url(r'^save_task/$', views.new_task, name='new_task'),
    url(r'^(?P<pk>\d+)/edit_task/$', views.edit_task, name='edit_task'),
    url(r'^(?P<pk>\d+)/delete_task/$', views.delete_task, name='delete_task'),
    url(r'^sign_out/$', views.sign_out, name='sign_out'),
]