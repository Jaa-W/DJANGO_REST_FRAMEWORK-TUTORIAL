from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True                                 # is method GET, HEAD itd in SAFE PERMISSION
        return obj.owner == request.user                # is user the owner of post