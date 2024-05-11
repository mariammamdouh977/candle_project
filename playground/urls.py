from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login, name="login"),
    path("checkout", views.checkout, name="checkout"),
    path("forgetPassword", views.forgetPassword, name="forgetPassword"),
    path("index", views.index, name="index"),
    path("products", views.products, name="products"),
    path("signup", views.signup, name="signup"),
    path("learnmore", views.learnmore, name="learnmore"),
]
