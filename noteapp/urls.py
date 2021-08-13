"""noteapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from notes.views import editor, delete_note

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    #path('', editor, name='editor'),
    path('delete_document/<int:noteid>', delete_note, name='delete_note'),
    #path('admin/', admin.site.urls),

    url(r"^", include("notes.urls")),
    url(r"^admin/", admin.site.urls),
]
