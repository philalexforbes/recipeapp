from django.db import models

# Create your models here.

class recipe(models.Model):
    RECIPE_TYPES = (
        ('BR', 'Breakfast'),
        ('LU', 'Lunch'),
        ('DI', 'Dinner'),
        ('DR', 'Drink'),
        ('DE', 'Dessert'),
    )
    recipe_name = models.CharField(max_length = 72)
    recipe_author = models.CharField(max_length = 30)
    recipe_type = models.CharField(max_length = 2, choices=RECIPE_TYPES)
    recipe_date_added = models.DateTimeField(auto_now_add=True)
    recipe_picture = models.FileField(upload_to='recipepics/') #need to figure out how to convert recipe name over to string

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class ingredients(models.Model):
    recipe = models.ForeignKey(recipe, models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text