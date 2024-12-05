from django.contrib import admin
from .models import Brand, CarModel, Comment, BuyNow

# Register your models here.
admin.site.register(Brand)
admin.site.register(CarModel)
admin.site.register(Comment)
admin.site.register(BuyNow)