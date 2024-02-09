

from django.urls import path
from.import views
# from .views import ProductDetailView


urlpatterns = [
    
    path('',views.store,name='store'),
    path('<slug:category_slug>/',views.store,name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/',views.product_detail ,name='product_detail'),
    # path('product/<slug:category_slug>/<slug:product_slug>/', ProductDetailView.as_view(), name='product-detail'),



] 




    