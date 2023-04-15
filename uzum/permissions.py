from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated


class IsAdminUserOrReadOnly(BasePermission):
    """
    Allows access only to admin ss or readonly.
    """

    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or request.user and request.user.is_staff)


class IsOwner(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if request.method == 'POST' and request.user.is_authenticated:
            return True
        return obj.user == request.user


class IsOwnerorReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.owner == request.user
