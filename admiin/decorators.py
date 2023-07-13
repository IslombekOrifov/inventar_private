from functools import wraps
from django.http import HttpResponseForbidden


def superuser_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Check if the user is a superuser
        if not request.user.is_superuser:
            return HttpResponseForbidden()

        # User is a superuser, proceed to execute the view
        return view_func(request, *args, **kwargs)

    return wrapper