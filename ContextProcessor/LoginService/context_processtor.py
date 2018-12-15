from .models import User


def frontContext(request):
    userId = request.session.get("userId")
    context = {}
    context["isLogin"] = False
    if userId:
        try:
            user = User.objects.get(pk = userId)
            context["isLogin"] = True
            context["user"] = user
        except :
            pass
    # print(request.__dict__)
    return context
