from rest_framework import serializers
from .models import User, Department


class UserModelSerializer(serializers.ModelSerializer):
    """用户序列化器"""

    class Meta:
        # 指定序列化的模型
        model = User
        # 指定序列化的字段
        fields = ("id", "username", "mobile", "department")


class DepartmentModelSerializer(serializers.ModelSerializer):
    """部门序列化器"""
    department = UserModelSerializer(many=True)

    class Meta:
        # 指定序列化的模型
        model = Department
        # 指定序列化的字段
        fields = ("id", "name", "leader", "num", "addr", "phone", "department")
