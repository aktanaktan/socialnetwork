from django.contrib.auth.models import User
from rest_framework import serializers
from newtask_api.models import Post, Like, DisLike


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True, required=True)
    password2 = serializers.CharField(min_length=6, write_only=True, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'password2')

    def validate(self, attrs):
        password2 = attrs.pop("password2")
        if attrs['password'] != password2:
            raise serializers.ValidationError("Password didn't match !")
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ("owner", "likes_number")


class DisLikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = DisLike
        fields = ("owner", "dislikes_number",)


class PostSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    likes = LikeSerializer(many=True, read_only=True)
    dis_likes = DisLikeSerializer(many=True, read_only=True)
    likes_number = LikeSerializer(many=False, read_only=True)
    dislikes_number = DisLikeSerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'owner', 'likes', 'dis_likes', "likes_number", "dislikes_number",)
