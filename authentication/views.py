from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework import generics, serializers
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.response import Response
from rest_framework import status

# ویو برای ثبت‌نام
class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
# --------------------------

# سریالایزر برای ورود
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)



# ویو برای ورود و تولید توکن
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer  # استفاده از سریالایزر ورود جدید
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)


# -------------------------------

# ویو برای لاگ اوت

class LogoutSerializer(serializers.Serializer):
    # ضوابط مورد نیاز
    pass

class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return LogoutSerializer

    def post(self, request):
        # بلاک کردن توکن فعلی
        try:
            # با توجه به `request.auth`، بلاک کردن توکن
            OutstandingToken.objects.filter(token=request.auth).delete()  # حذف توکن
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# ------------------------

# ویو برای تولید توکن جدید

class CustomTokenRefreshView(TokenRefreshView):
        permission_classes = [AllowAny]
