from django.contrib.auth.models import AbstractUser

from models import BaseModel, models


class Department(BaseModel):
    """部门表"""
    leader = models.CharField(max_length=255, verbose_name="部门负责人")
    num = models.IntegerField(default=0, verbose_name="部门人数")
    addr = models.TextField(default='', verbose_name="部门地址")
    phone = models.CharField(default='', max_length=15, verbose_name='部门电话')

    class Meta:
        db_table = 'exam_department'
        verbose_name = '部门信息表'
        verbose_name_plural = verbose_name


class User(AbstractUser):
    """用户表"""
    mobile = models.CharField(max_length=15, verbose_name='手机号码')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='所属部门',
                                   db_constraint=False, related_name='department', null=True,
                                   blank=True)

    class Meta:
        db_table = 'exam_users'
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name
