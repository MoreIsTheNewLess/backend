from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'', views.login.as_view() , name="sireeshlogin"),
]
