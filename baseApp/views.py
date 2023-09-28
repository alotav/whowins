# Create your views here.
from rest_framework import viewsets
from .serializer import AppUsersSerializer
from .models import AppUsers

class AppUsersView(viewsets.ModelViewSet):
    serializer_class = AppUsersSerializer
    queryset = AppUsers.objects.all()