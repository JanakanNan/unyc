from rest_framework import permissions

class MyCustomPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True

        return request.user and request.user.is_staff