from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']

