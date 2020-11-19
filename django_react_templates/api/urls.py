from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),

    path('csrf/', views.get_csrf, name='api-csrf'),
    path('whoami/', views.check_session, name='api-whoami'),
    path('login/', views.login_view, name='api-login'),
    path('logout/', views.logout_view, name='api-logout'),
]
