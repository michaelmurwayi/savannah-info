from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('social-auth/', include('social_django.urls', namespace='social')),
]