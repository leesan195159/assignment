from django.urls import path, include

urlpatterns = [
    path("assignment", include('owners.urls'))
]
