def makeHelloWordMakeware(getResponse):

    print("初始化HelloWorldMakeWare构造器")
    def makeWare(request):

        print("请求在请求函数之前得到处理")
        response = getResponse(request)
        print("响应在到达浏览器之前得到处理")
        return response

    return makeWare


class MakeWareHelloWorld:

    def __init__(self, getResponse):
        print("初始化MakeWareHelloWorld类")
        self.__getResponse = getResponse
    
    def __call__(self, request):
        print("类处理器:请求在请求函数之前得到处理")
        response = self.__getResponse(request)
        print("类处理器:响应在到达浏览器之前得到处理")
        return response
