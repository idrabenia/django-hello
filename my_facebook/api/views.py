from django.contrib.auth.models import Group
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from api.serializers import UserSerializer, GroupSerializer
from users.models import User


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'user-list': reverse('api:user-list', request=request, format=format),
        'group-list': reverse('api:group-list', request=request, format=format)
    })


class UserList(ListCreateAPIView):
    model = User
    serializer_class = UserSerializer


class UserDetails(RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer


class GroupList(ListCreateAPIView):
    model = Group
    serializer_class = GroupSerializer


class GroupDetails(RetrieveUpdateDestroyAPIView):
    model = Group
    serializer_class = GroupSerializer