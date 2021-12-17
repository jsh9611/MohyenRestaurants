"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # admin/ 이라면 admin.site.urls 에서 처리한다.
    path('map/', include('map.urls')), # map/ 이라면 map.urls 에서 처리한다.
    path('board/', include('board.urls')), # board/ 라면 board.urls 에서 처리한다.
    path('', include('page.urls')), # url 에 아무것도 입력되지 않는다면 page.urls 에서 처리한다.
    path('accounts/', include('allauth.urls')), # accounts/ 라면 allauth.urls 에서 처리한다.
    path('markdownx/', include('markdownx.urls')), # markdownx/ 라면 markdownx.urls 에서 처리한다.
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # static 파일들을 가져오기 위해 추가