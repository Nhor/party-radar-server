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


class GetPostsSerializer(serializers.Serializer):
    lat = serializers.FloatField()
    lon = serializers.FloatField()
    radius = serializers.IntegerField()
    time_offset = serializers.IntegerField()


class GetPostsResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.CharField()
    photo = serializers.ImageField()
    description = serializers.CharField(required=False)
    lat = serializers.FloatField()
    lon = serializers.FloatField()
    created = serializers.DateTimeField()
    modified = serializers.DateTimeField()
