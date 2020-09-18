from django.contrib.auth.models import Group, Permission
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from userapp import models
from userapp.authenticator import MyAuth
from userapp.permission import MyPermission
from userapp.throttle import MyThrottle


class Demo(APIView):
    def get(self, request, *args, **kwargs):
        # user = models.User.objects.first()
        # print(user.email, user.groups.first().name, user.user_permissions.first().name)

        # group = Group.objects.first()
        # print(group, group.user_set.first().username, group.permissions.first())

        # permission = Permission.objects.first()
        # print(permission.name, permission.user_set.first().username)
        # per = Permission.objects.filter(pk=1).first()
        # print(per.group_set.first().name)

        return Response("OK")


class UserAPIView(APIView):

    permission_classes = [MyPermission]
    authentication_classes = [MyAuth]
    throttle_classes = [MyThrottle]

    def get(self, request, *args, **kwargs):
        return Response("读操作")

    def post(self, request, *args, **kwargs):
        return Response("写操作")
