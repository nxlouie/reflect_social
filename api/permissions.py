from rest_framework.permissions import BasePermission
from .models import Contact
from .models import Interaction


class IsOwner(BasePermission):
    """Custom permission class"""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the object owner."""
        if isinstance(obj, Contact) or isinstance(obj, Interaction):
            return obj.owner == request.user
        return obj.owner == request.user
