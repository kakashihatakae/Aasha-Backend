from django.urls import path
from .views import UserProfilesGetPost, kaka


urlpatterns = [
    path('', kaka.as_view())
]
