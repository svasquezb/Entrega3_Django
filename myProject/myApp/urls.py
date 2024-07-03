from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("", views.index, name="index"),
    path("productos", views.productos, name="products"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("carro", views.carro, name="carro"),
    path("detalleJuego", views.detalleJuego, name="detalleJuego"),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
