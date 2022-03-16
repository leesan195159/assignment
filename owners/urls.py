from django.urls import path

from .views import *

urlpatterns = [
    path('/owners', OwnerView.as_view()),
    path('/dogs', DogView.as_view()),
]