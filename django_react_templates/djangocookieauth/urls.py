from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include


def index_view(request):
    return render(request, 'dist/index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', index_view, name='index'),
]
