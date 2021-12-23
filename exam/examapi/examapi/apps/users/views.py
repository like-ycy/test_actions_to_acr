from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .models import User, Department
from .serializers import UserModelSerializer, DepartmentModelSerializer


class UserViewSet(ModelViewSet):
    """用户接口视图"""
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class DepartmentPagination(PageNumberPagination):
    """部门分页"""
    page_size = 5  # 默认分页的每一页数据量
    max_page_size = 20  # 设置允许客户端通过地址栏参数调整的最大单页数据量
    page_size_query_param = "size"


class DepartmentViewSet(ModelViewSet, PageNumberPagination):
    """部门接口视图"""
    queryset = Department.objects.all()
    serializer_class = DepartmentModelSerializer

    pagination_class = DepartmentPagination
