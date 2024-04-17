from django.views.generic import TemplateView


class MenuView(TemplateView):
    template_name = "menu/menu.html"


__all__ = ()
