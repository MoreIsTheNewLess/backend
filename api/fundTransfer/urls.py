from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'', views.fundTransfer.as_view() , name="transfer"),
]
