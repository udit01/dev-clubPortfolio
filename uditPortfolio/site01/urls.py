from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^hobbies/', views.hobbies, name='hobbies'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^social/', views.social, name='social'),
    # url(r'^about/',
    # url(r'^site01/',
    # url(r'^site01/',
    # url(r'^site01/',
    # url(r'^site01/',
]
