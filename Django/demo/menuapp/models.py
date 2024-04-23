from django.db import models

# Create your models here.
class Menu(models.Model): 
    menu_name = models.CharField(max_length=100)  
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()
    rating = models.FloatField()

    def __str__(self):
        return self.name + " : " + self.cuisine + " : " + str(self.price) + " : " + str(self.rating)