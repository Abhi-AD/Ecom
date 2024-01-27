from django.urls import path
from store import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("login_user/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register_user/", views.register_user, name="register_user"),
    path("product/<int:pk>", views.product, name="product"),
    path("category/<str:foo>", views.category, name="category"),
]
