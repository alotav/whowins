from rest_framework import serializers
from .models import AppUsers

class AppUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUsers
        # fields = ('id', 'name', 'lastname', 'email')
        fields = '__all__'