from django.urls import path

from menu.views import MenuView

app_name = "menu"
urlpatterns = [
    path("", MenuView.as_view(), name="home"),
    path("contacts/", MenuView.as_view(), name="contacts"),
    path("contacts/ceo/", MenuView.as_view(), name="ceo"),
    path("contacts/manager/", MenuView.as_view(), name="manager"),
    path("contacts/leads/", MenuView.as_view(), name="leads"),
    path("contacts/leads/python/", MenuView.as_view(), name="python"),
    path("contacts/leads/goland/", MenuView.as_view(), name="golang"),
    path("location/", MenuView.as_view(), name="location"),
    path("location/office/", MenuView.as_view(), name="office"),
    path("menu/", MenuView.as_view(), name="menu"),
    path("menu/account/", MenuView.as_view(), name="account"),
    path("menu/friends/", MenuView.as_view(), name="friends"),
    path("menu/news/", MenuView.as_view(), name="news"),
    path("menu/news/hot/", MenuView.as_view(), name="news_hot"),
    path("menu/news/ice/", MenuView.as_view(), name="news_ice"),
]
