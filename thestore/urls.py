"""
URL configuration for thestore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from app1 import views
from django.conf import settings
from django.conf.urls.static import static


from app1.views import contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('page_links', views.page_links),

    # home
    path('', views.base_index),
    path('base_index', views.base_index),
    path('index/<int:customer_id>/', views.index, name='index'),
    path('index/<int:customer_id>/back_index', views.back_home, name='back_index'),  # profile
    path('index/<int:customer_id>/view_product/<int:product_id>/back_index', views.back_home1, name='back_index'),  # product

    # store
    path('blank', views.blank),
    path('checkout', views.checkout),


    path('cart', views.cart),
    path('all_products', views.all_products),
    path('all_stores', views.all_stores),

    #  user
    path('my_view', views.my_view),
    path('login', views.login_user),
    path('signup', views.signup_customer),
    path('signup_customer', views.signup_customer),
    path('logout_view', views.logout_view),

    # supplier
    path('supplier_portal', views.supplier_portal),
    path('signup_supplier', views.signup_supplier),
    path('supplier_login', views.supplier_login),
    path('supplier_view', views.supplier_view),


    # admin
    path('admin_portal', views.admin_portal),
    path('signup_admin', views.signup_admin),
    path('admin_login', views.admin_login),
    path('admin_view', views.admin_view),

    # contact

    path('contact', views.contact_view),

    path('message', views.messages_view),

    # Product
    path('create_product/<int:supplier_id>/create_product', views.create_product),
    path('create_product/<int:supplier_id>/', views.create_product, name='create_product'),

    path('supplier/<int:supplier_id>/', views.products_by_supplier, name='products_by_supplier'),
    path('delete_product/<int:product_id>', views.delete_product, name='delete_product'),

    path('index/<int:customer_id>/product_category', views.product_category),
    path('product_category_by_id', views.product_category_by_id, name='product_category_by_id'),



    path('index/<int:customer_id>/profile', views.profile, name='profile'),
    path('index/<int:customer_id>/view_product/<int:product_id>/profile1', views.profile1, name='profile1'),
    path('index/<int:customer_id>/Account_Dashboard', views.Account_Dashboard, name='Account_Dashboard'),
    path('index/<int:customer_id>/edit_customer_details', views.edit_customer_details, name='edit_customer_details'),


    path('index/<int:customer_id>/view_product/<int:product_id>/', views.view_product, name='view_product'),


    path('index/<int:customer_id>/view_cart', views.view_cart, name='view_cart'),
    path('index/<int:customer_id>/view_product/<int:product_id>/view_cart1', views.view_cart1, name='view_cart1'),
    path('index/<int:customer_id>/view_product/<int:product_id>/add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('index/<int:customer_id>/remove_from_cart/<str:product_id>/', views.remove_from_cart, name='remove_from_cart')
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
