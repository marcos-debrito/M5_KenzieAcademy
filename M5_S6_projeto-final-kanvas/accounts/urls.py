from django.urls import path
from rest_framework_simplejwt import views
from .views import AccountView


urlpatterns = [
    path("login/", views.TokenObtainPairView.as_view()),
    path("accounts/", AccountView.as_view()),
]
