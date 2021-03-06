from rest_framework import serializers
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'password', )