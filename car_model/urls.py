from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('add_car/', AddCarView.as_view(), name='addCar'),
    path('add_brand/', AddBrandView.as_view(), name='addBrand'),
    path('edit_car/<int:id>', EditCarView.as_view(), name='editCar'),
    path('edit_brand/<int:id>', EditBrandView.as_view(), name='editBrand'),
    # path('show_details/<int:id>', details_post_view, name='show_details'),
    path('show_details/<int:id>', DetailsPostView.as_view(), name='show_details'),
    path('buynow/<int:id>', buy_now, name='buynow'),
    path('filter_by_brand/<int:brand_id>', view_car_by_brand, name='bybrand'),
]