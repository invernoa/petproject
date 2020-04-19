from .views import *
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('dogs/', Dogs.as_view()),
    path('kennels/', Kennels.as_view()),
    path('breeds/', Breeds.as_view()),
    # path('dogs/', DogDetails.as_view())
    # path('add_dogs/', Dogs.as_view()),
    url(r'^dogs/(?P<pk>[0-9]+)/$', DogDetails.as_view(), name='dog-detail')
]
