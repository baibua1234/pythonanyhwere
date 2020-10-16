from django.forms import ModelForm
from django import forms

from .models import Food,FoodType

class addFoodType(ModelForm):
    class Meta:
        model = FoodType
        fields = ['Food_Type']


class addFood(ModelForm):
    class Meta:
        model = Food
        fields = ['Food_Name','Price','Calorie','FoodType']






