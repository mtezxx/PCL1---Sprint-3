"""
URL configuration for gtg_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cafe.views import product_list, place_order, product_create, product_update, product_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='product_list'),
    path('order/', place_order, name='place_order'),
    path('product/create/', product_create, name='product_create'),
    path('product/<int:pk>/edit/', product_update, name='product_update'),
    path('product/<int:pk>/delete/', product_delete, name='product_delete'),
]
