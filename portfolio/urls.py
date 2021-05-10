"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from imtinan import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('blog/',views.blog,name='blog'),
    path('blog/<int:blog_id>/',views.blog_read,name='blog_read'),
    path('blog/<str:blog_tag>/',views.blog_detailed,name='blog_detailed'),
    path('contact/',views.contact_form,name='contact'),
    path('project/',views.project,name='project'),
    path('about/',views.about,name='about'),
    path('photos/',views.photos,name='photos'),
    

]



urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
