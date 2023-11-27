from .models import Account
from .serializers import AccountSerializer
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt import views


class AccountView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class LoginJWTView(views.TokenObtainPairView):
    serializer_class = AccountSerializer.CustomJWTSerializer
