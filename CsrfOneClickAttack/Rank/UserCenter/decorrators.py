from django.shortcuts import redirect, reverse
from .models import User

def loginDecorator(func):
    def inner(request, *args, **kwargs):
        # userId = request.session.get("userId")        
        # if userId:
            # exists = User.objects.filter(pk=userId).exists
        if request.frontUser:
            return func(request, *args, **kwargs)
        return redirect(reverse("UserView:Login"))
            
    return inner