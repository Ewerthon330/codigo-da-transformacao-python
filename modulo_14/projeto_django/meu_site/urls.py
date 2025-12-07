from django.contrib import admin
from django.urls import path, include
from produtos import views

urlpatterns = [
    path('', views.lista_produtos),   # agora "/" mostra a lista de produtos
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')),
]
