"""VoiceAssistant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include, static
from django.contrib import admin
from search.views import index,addEdu,addProject,addExp,jobDetail,process
from django.conf.urls import include ,url
from django.conf import settings 
from django.contrib.auth import views as auth_views
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^addEdu/', addEdu ,name='addEdu' ),
    url(r'^addProject/', addProject ,name='addProject' ),
    url(r'^process/', process ,name='process' ),    
    url(r'^addExp/', addExp ,name='addExp' ),
    url(r'^job/(?P<id>\d+)/$', jobDetail, name='jobDetail'),     
    url(r'^(?P<string>[\w\-]+)/$',index,name='index'),
]

if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
