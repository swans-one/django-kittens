from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^random/$', views.random_kitten_view, name='random-kitten'),
    url(r'^up/(?P<id>[0-9]*)/$', views.kitten_up, name='kitten-up'),
    url(r'^down/(?P<id>[0-9]*)/$', views.kitten_down, name='kitten-down'),
    url(r'^top/', views.top_kittens, name='top-kittens'),
]
