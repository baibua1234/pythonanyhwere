from django.db import models

class Calorie(models.Model):

    id = models.AutoField(primary_key=True)

    Calorie = models.IntegerField(default="แคลลอรี่")

    def __str__(self):
        return f'{self.Calorie}'

class FoodType(models.Model):
    id = models.AutoField(primary_key=True)
    Food_Type = models.CharField(max_length=100,default="ประเภทอาหาร")

    def __str__(self):
        return f'{self.Food_Type}'

class Food(models.Model):
    Food_Name = models.CharField(max_length=100)
    Price = models.IntegerField()

    Calorie = models.ForeignKey(Calorie, on_delete=models.CASCADE)
    FoodType = models.ForeignKey(FoodType, on_delete=models.CASCADE)

    def __str__(self):

        return f'{self.Food_Name} - {self.FoodType} - {self.Calorie} - {self.Price}'
