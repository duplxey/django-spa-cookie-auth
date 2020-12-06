from django.urls import path

from . import views
from .views import SessionView

urlpatterns = [
    path('csrf/', views.get_csrf, name='api-csrf'),
    path('login/', views.login_view, name='api-login'),
    path('logout/', views.logout_view, name='api-logout'),
    path('session/', SessionView.as_view(), name='api-session'),
]
