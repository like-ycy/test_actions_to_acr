from rest_framework.serializers import ModelSerializer

from .models import User, Department


class UserModelSerializer(ModelSerializer):
    """用户序列化器"""

    class Meta:
        # 指定序列化的模型
        model = User
        # 指定序列化的字段
        fields = ("id", "username", "mobile", "department")


class DepartmentModelSerializer(ModelSerializer):
    """部门序列化器"""

    class Meta:
        # 指定序列化的模型
        model = Department
        # 指定序列化的字段
        fields = ("id", "name", "leader", "num", "addr", "phone")
