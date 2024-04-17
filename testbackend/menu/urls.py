from django.urls import path

from menu.views import ContactSeoView, ContactView, LocationView, MenuView

app_name = "menu"
urlpatterns = [
    path("", MenuView.as_view(), name="home"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("contacts/ceo/", ContactSeoView.as_view(), name="seo"),
    path("location/", LocationView.as_view(), name="location"),
    path("contacts/max", LocationView.as_view(), name="max"),
]
