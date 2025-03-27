from rest_framework.permissions import BasePermission, DjangoModelPermissions
from datetime import datetime


class OwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["HEAD", "OPTIONS", "GET"]:
            return True
        return obj.owner == request.user


class IsWorkHour(BasePermission):
    def has_permission(self, request, view):
        hour = datetime.today().hour
        return 9 <= hour <= 17


class CustomModelPermissions(DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.add_%(model_name)s'],
        'OPTIONS': ['%(app_label)s.add_%(model_name)s'],
        'HEAD': ['%(app_label)s.add_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }