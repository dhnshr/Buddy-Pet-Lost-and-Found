from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sentry", views.sentry, name="sentry"),
    path("login", views.loginView, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logoutView, name="logout"),
    path("missing", views.newMissing, name="missing"),
    path("sight", views.newSight, name="sighting"),
    path("shop",views.shop,name="shop"),
    path("adoption",views.adoption,name="adoption"),
    path("Adoption1",views.Adoption1,name="Adoption1"),
    path("Adoption2",views.Adoption2,name="Adoption2"),
]