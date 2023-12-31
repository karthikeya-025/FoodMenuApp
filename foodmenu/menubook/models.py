from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Items(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg",
    )
