from django.contrib import admin

from .models import Question, Choice, FoodType, Food

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(FoodType)
admin.site.register(Food)
