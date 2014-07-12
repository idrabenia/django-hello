from django.contrib.auth.models import Group
from rest_framework import serializers
from users.models import User, Address


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('country', 'city', 'address1', 'address2', 'address3')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:user-detail')
    primary_address = AddressSerializer()

    class Meta:
        model = User
        fields = ('id', 'url', 'first_name', 'last_name', 'email', 'birth_year', 'primary_address')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:group-detail')
    permissions = serializers.SlugRelatedField(slug_field='codename', many=True)

    class Meta:
        model = Group
        fields = ('url', 'name', 'permissions')
