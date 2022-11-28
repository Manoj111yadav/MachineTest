from django.urls import re_path
from taskapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^Client$',views.ClientApi),
    re_path(r'^Client/([0-9]+)$',views.ClientApi),

    re_path(r'^User$',views.UserApi),
    re_path(r'^User/([0-9]+)$',views.UserApi),

    re_path(r'^Project$',views.ProjectApi),
    re_path(r'^Project/([0-9]+)$',views.ProjectApi),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
