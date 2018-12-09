from django.views.generic.base import View
from django.views.generic import TemplateView
from django.shortcuts import render


class BaseView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "baseview_get.html")

    def get(self, request, bookId):
        return render(request, "baseview_path.html")

    def post(self, request, *args, **kwargs):
        return render(request, "baseview_post.html")

    def http_method_not_allowed(self, request, *args, **kwargs):
        return render(request, "error.html")

    def dispatch(self, request, *args, **kwargs):
        print("dispath")
        return super().dispatch(request, *args, **kwargs)


class AboutView(TemplateView):

    template_name = "tempate_view.html"

    def get_context_data(self, **kwargs):
        context = {'username': "TemplateViewTest"}
        return context