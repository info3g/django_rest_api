from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Student

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name', 'last_name', 'is_staff')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'address', 'contact')
        # fields = "__all__"