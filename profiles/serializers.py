from rest_framework import serializers

from profiles.models import User, Section, Subscription


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'about', 'is_coach')
        read_only_fields = ('email')


class SectionSerializer(serializers.ModelSerializer):
    """
    Section serializer
    """

    class Meta:
        model = Section
        fields = ('name', 'coach', 'info',
                  'price', 'schedule', 'date_created')
        read_only_fields = ('date_created', 'coach')


class SubscriptionSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(read_only=True)
    subscription = SectionSerializer(read_only=True)

    class Meta:
        model = Subscription
        fields = ('user', 'subscription', 'date_started')
        read_only_fields = ('date_started')
