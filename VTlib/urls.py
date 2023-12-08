"""VTlib URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # 追記
from django.conf.urls.static import static # 追記

from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
index_view = TemplateView.as_view(template_name="website/logined.html")
from website import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('social-auth/', include('allauth.urls')), #API 
    path('', include("django.contrib.auth.urls")),
    path("", login_required(index_view), name="index"),
    path("", include("website.urls")),
    #path('activate/<uidb64>/<token>/', views.ActivateView.as_view(), name='activate'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 追記


