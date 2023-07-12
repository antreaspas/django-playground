from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission that allows only the author of a blog model to update or delete it.
    """

    def has_object_permission(self, request, view, obj):
        return True if request.method in permissions.SAFE_METHODS else obj.author == request.user
