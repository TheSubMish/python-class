from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


class IsAdminUser(BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.role == "admin":
            return True
        raise PermissionDenied("You do not have permission to perform this action.")
