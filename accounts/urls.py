from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name':'accounts/login.html'
    }, name= 'login' ),
    url(r'^logout/$', auth_views.logout, {'template_name':'accounts/logout.html'
    }, name='logout'),
    url(r'^perfil/$',TemplateView.as_view(template_name="accounts/profile.html"),
    name='perfil'),
]
