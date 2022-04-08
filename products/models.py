from django.db import models

class menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menu'

class category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'category'

class drink(models.Model):
    korean_name     = models.CharField(max_length=45)
    english_name     = models.CharField(max_length=45)
    description     = models.TextField
    category = models.ForeignKey('category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'drink'

class image(models.Model):
    image_url     = models.CharField(max_length=2000)
    drink = models.ForeignKey('drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'image'

class allergy(models.Model):
    name     = models.CharField(max_length=45)

    class Meta:
        db_table = 'allergy'

class allergy_drink(models.Model):
    allergy = models.ForeignKey('allergy', on_delete=models.CASCADE)
    drink = models.ForeignKey('drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergy_drink'


class nutrition(models.Model):
    one_serving_kca     = models.DecimalField(max_digits=10, decimal_places=2)
    sodium_kca     = models.DecimalField(max_digits=10, decimal_places=2)
    saturated_fat_mg     = models.DecimalField(max_digits=10, decimal_places=2)
    sugars_g     = models.DecimalField(max_digits=10, decimal_places=2)
    protein_g     = models.DecimalField(max_digits=10, decimal_places=2)
    caffeine_mg     = models.DecimalField(max_digits=10, decimal_places=2)
    drink = models.ForeignKey('drink', on_delete=models.CASCADE)
    size = models.ForeignKey('size', on_delete=models.CASCADE)

    class Meta:
        db_table = 'nutrition'

class size(models.Model):
    name     = models.CharField(max_length=45)
    size_ml     = models.CharField(max_length=45)
    size_fluid_ounce     = models.CharField(max_length=45)

    class Meta:
        db_table = 'size'

# Create your models here.
