from django.urls import path

from .views import ActorView, MovieView

urlpatterns = [
    path('/ac', ActorView.as_view()),
    path('/mo', MovieView.as_view())
]
