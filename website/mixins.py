from django.shortcuts import redirect
from django.conf import settings

class RedirectAuthenticatedUserMixin:
    """
    Mixin to redirect authenticated users away from certain views (like login or signup).
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
          # If the user is authenticated, redirect them to the specified URL
            return redirect(settings.LOGIN_REDIRECT_URL)
          # Otherwise, proceed as normal
        return super().dispatch(request, *args, **kwargs)