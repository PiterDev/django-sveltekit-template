from dj_rest_auth.views import LoginView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAdminUser

class TestView(APIView):
    def get(self, request):
        data = {'message': 'Hello, from the API!'}
        return Response(data)


class AdminView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        data = {'message': 'Hello, from the admin API!'}
        return Response(data)