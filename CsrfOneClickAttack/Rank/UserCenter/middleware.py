from .models import User

def makeUserMiddleware(getResposne):

    def makeware(request):
        userId = request.session.get("userId")
        if userId:
            user = User.objects.filter(pk=userId).first()
            if user:
                request.frontUser = user
            else:
                request.frontUser = None
        else:
            request.frontUser = None
        response = getResposne(request)
        return response

    return makeware