from django.urls import path
from . import views

urlpatterns = [
    path('whoami/', views.check_session, name='api-whoami'),
    path('login/', views.login_view, name='api-login'),
    path('logout/', views.logout_view, name='api-logout'),
]
