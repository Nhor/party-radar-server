from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()


class SubmitPostSerializer(serializers.Serializer):
    photo = serializers.ImageField()
    description = serializers.CharField(required=False)
    lat = serializers.FloatField()
    lon = serializers.FloatField()
