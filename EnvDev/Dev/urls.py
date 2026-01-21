from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path("municipalitypage/", views.municipalitypage, name="municipalitypage"),
    path("bins/", views.bins_view, name="bins"),
    path("truck/", views.truck_dashboard, name="truck_dashboard"),
    path("factory/", views.factory_interface, name="factory_interface"),
    path("index/", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("map/", views.map_view, name="map"),
    path("report/", views.report, name="report"),
    path("analytics/", views.analytics, name="analytics"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("collection/", views.collection, name="collection"),
]