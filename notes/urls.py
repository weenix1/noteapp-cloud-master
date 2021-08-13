# notes/urls.py

from django.conf.urls import include, url
from notes.views import dashboard, register, editor

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^register/", register, name="register"),
    url(r"^editor/", editor, name="editor"),
    url(r"^", dashboard, name="dashboard"),
]
