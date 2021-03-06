"""musiikkihaku URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from musicsearch import views as ms_views

urlpatterns = [
    url(r'^$', ms_views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', ms_views.login_user, name='login'),
    url(r'^signup/$', ms_views.create_user, name='signup'),
    #url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout/$', ms_views.logout_user, name='logout'),
    url(r'^musicsearch/', include('musicsearch.urls'))
]
