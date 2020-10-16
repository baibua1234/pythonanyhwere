from django.contrib import admin

from .models import Calorie, FoodType, Food


admin.site.register(FoodType)
admin.site.register(Food)
admin.site.register(Calorie)
