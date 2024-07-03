from . import views
from django.urls import path
urlpatterns = [
    path("", views.index, name="index"),
    path("productos", views.productos, name="products"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("carro", views.carro, name="carro"),
    path("detalleJuego", views.detalleJuego, name="detalleJuego"),

]