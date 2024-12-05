from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='brand_images', blank=True, null=True)

    def __str__(self):
        return self.name
    

class CarModel(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='car_images', blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}  {self.brand}"


class BuyNow(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buynow')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.car}  {self.user}"


class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment_text = models.TextField()
    post = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}  {self.comment_text}"