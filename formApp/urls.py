from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.contact_form, name="index"),
    # url(r'^add/$', views.add, name="add"),
    url(r'^success/$', views.show, name="show"),
    url(r'^register/$', views.Register.as_view(), name='accounts-register'),
    url(r'^login/$', views.Login.as_view(), name='accounts-login'),
]
