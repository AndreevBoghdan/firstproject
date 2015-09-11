
from django.conf.urls import include, url
from article import views


urlpatterns = [
    url(r'^1/', views.basic_one, name="basic_one"),
    url(r'^2/', views.template_two, name="template_two"),
    url(r'^3/', views.template_three_simple, name="template_three_simple"),
    url(r'^articles/all/$', views.articles, name="articles"),

    url(r'^page/(?P<page_number>\d+)/$', views.articles, name="articles"),

    url(r'^articles/get/(?P<article_id>\d+)/$', views.article, name="article"),
    url(r'^articles/addlike/(?P<article_id>\d+)/(?P<page_number>\d+)/$', views.addlike, name="addlike"),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', views.addcomment, name="addcomment"),
  	
  	url(r'^', views.articles, name="articles"),
    
]
