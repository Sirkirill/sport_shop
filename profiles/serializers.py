from rest_framework import serializers

from profiles.models import User, Section, Subscription


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'about', 'is_coach')
        read_only_fields = 'email'


class SectionSerializer(serializers.ModelSerializer):
    """
    Team serializer
    """
    section = serializers.PrimaryKeyRelatedField(read_only=True)
    creator = serializers.SerializerMethodField()
    device = serializers.SerializerMethodField(read_only=True)

