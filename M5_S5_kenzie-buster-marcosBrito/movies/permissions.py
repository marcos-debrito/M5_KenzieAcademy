from rest_framework import permissions
from rest_framework.views import Request, View


class MoviesPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.is_employee:
            return True

        return False
