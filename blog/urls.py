from django.urls import re_path, include
from . import views
from django.contrib import admin

urlpatterns = [
    # re_path(r'^admin/', admin.site.re_paths),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^posts/$', views.post_list, name='post_list'),
    re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    re_path(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    re_path(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    re_path(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    re_path(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    re_path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    re_path(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    re_path(r'^about_me/$', views.about_me, name='about_me'),
    re_path(r'^portfolio/$', views.portfolio_list, name="portfolio_list"),
    re_path(r'^category/(?P<pk>\d+)/$', views.category_detail, name='category_detail'),

]
