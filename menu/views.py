from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = "menu/index.html"


class Index1PageView(TemplateView):
    template_name = "menu/index1.html"
