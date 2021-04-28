from django.urls import path
from cekbpom_license import views

urlpatterns = [

    path('home', views.home, name = 'home'),
    path('by_product', views.query_by_product, name = 'query_by_product'),
	path('by_product_name', views.query_by_product_name, name = 'query_by_product_name'),
	path('by_brand', views.query_by_brand, name = 'query_by_brand'),
	path('by_registrant', views.query_by_registrant, name = 'query_by_registrant'),
	path('by_producer', views.query_by_producer, name = 'query_by_producer'),
	path('by_validity', views.query_by_validity, name = 'query_by_validity'),
    
    ]