# urls
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from . import views

app_name = 'accounts'
urlspattern = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh', TokenRefreshView.as_view(), name='token-refresh'),
    path('me/', views.ProfileView.as_view(), name='profile')
]