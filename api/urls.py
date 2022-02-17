from django.urls import path
from . import views

urlpatterns = [
    path("phases/", views.getAllPhase, name="all_phase"),
    path("phase/<str:pk>/", views.getPhase, name="get_phase"),
    path("locks/", views.getAllLock, name="all_lock"),
    path("lock/<str:pk>/", views.getLock, name="get_lock"),
]
