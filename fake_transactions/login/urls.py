from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'', views.fake_transactions.as_view() , name="fake_transactions"),
]
