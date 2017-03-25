from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

from hackathon import views

router = DefaultRouter()

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^api/$', views.api_examples, name='api'),
    url(r'^linkedin_login/$', views.linkedin_login, name='linkedin_login'),
    url(r'^facebook_login/$', views.facebook_login, name='facebook_login'),
    url(r'^facebook/$', views.facebook, name='facebook'),
    url(r'^offers/$', views.OfferView.as_view(), name='offers'),
)
