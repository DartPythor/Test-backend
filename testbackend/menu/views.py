from django.views.generic import TemplateView


class MenuView(TemplateView):
    template_name = "menu/menu.html"


class ContactView(TemplateView):
    template_name = "menu/menu.html"


class ContactSeoView(TemplateView):
    template_name = "menu/menu.html"


class LocationView(TemplateView):
    template_name = "menu/menu.html"


__all__ = ()
