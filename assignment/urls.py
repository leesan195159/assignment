from django.urls import path, include

urlpatterns = [
    path('movies', include('movies.urls')
    path("assignment", include('owners.urls'))
]
