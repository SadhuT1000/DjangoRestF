from rest_framework import permissions


class IsModer(permissions.BasePermission):
    """Проверяет, является ли пользователь модератором."""

    message = "Ты не достоЕН так как не модератор!!"

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moders").exists()


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """Проверяет, является ли пользователь владельцем."""

        if obj.owner == request.user:
            return True
        return False
