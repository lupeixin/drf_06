"""
1. 继承`BasePermission`
2. 实现`has_permission`方法，根据自定义规则实现权限，全局或局部配置
"""
from rest_framework.permissions import BasePermission

from userapp.models import User


class MyPermission(BasePermission):
    """
    有权访问返回True
    无权访问返回False
    登录可写  游客只读
    """
    def has_permission(self, request, view):

        # 如果是制度接口， 则所有人都可以访问
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True

        username = request.data.get("username")

        # 如果用户访问是写操作 判断用户是否有登录信息
        user = User.objects.filter(username=username).first()
        if user:
            return True
        return False
