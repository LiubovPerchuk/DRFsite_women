from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Класс разрешений для доступа только администратору объекта."""

    def has_permission(self, request, view):
        """Метод предоставляет разрешение администратору объекта."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
