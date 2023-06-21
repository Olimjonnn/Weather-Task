from django.urls import path
from main.views import InfoView, InfooView
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
) 

urlpatterns = [
    path("info/", InfoView.as_view()),
    path("infoo/", InfooView.as_view()),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
]