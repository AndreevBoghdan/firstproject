
from django.conf.urls import include, url
from loginsys import views


urlpatterns = [
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^register/$', views.register, name="register"),
    url(r'^recoverlogin/$', views.recoverlogin, name="recoverlogin"),
  	
  	
]
