from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from . import views

router = DefaultRouter()
router.register('info', views.UserViewSet, basename='user')
router.register('department', views.DepartmentViewSet, basename='department')

urlpatterns = [
                  path('login/', obtain_jwt_token, name='login'),
              ] + router.urls
