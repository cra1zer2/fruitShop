from django.contrib import admin
from django.urls import path, include
from shop_app import views as shop_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shop_views.strona_glowna, name='strona_glowna'),
    path('', include('shop_app.urls')),
]