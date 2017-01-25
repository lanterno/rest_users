from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^suspend-account/$', views.SuspendAccountView.as_view(), name='suspend_account'),
    url(r'^', include('djoser.urls.authtoken')),
]
