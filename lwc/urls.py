"""lwc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from joins import views as joinsView
from lwc import views as lwcView

# from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', joinsView.home, name='home'),
    # url(r'^testhome$', lwcView.testhome, name='testhome'),
    url(r'^(?P<ref_id>.*)$', joinsView.share, name='share'),
]
