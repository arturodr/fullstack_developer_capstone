# Uncomment the following imports before adding the Model code

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    """
    Modelo para representar marcas de automóviles
    """
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción", blank=True)
    country_of_origin = models.CharField(max_length=100,
                                         verbose_name="País de origen",
                                         blank=True)

    # Metadatos para el modelo
    class Meta:
        verbose_name = "Marca de automóvil"
        verbose_name_plural = "Marcas de automóviles"
        ordering = ['name']

    def __str__(self):
        return self.name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    """
    Modelo para representar modelos específicos de automóviles
    """
    class CarType(models.TextChoices):
        SEDAN = 'SEDAN', 'Sedán'
        SUV = 'SUV', 'SUV'
        WAGON = 'WAGON', 'Wagon'
        HATCHBACK = 'HATCHBACK', 'Hatchback'
        COUPE = 'COUPE', 'Coupé'

    car_make = models.ForeignKey(
        CarMake,
        on_delete=models.CASCADE,
        related_name='models',
        verbose_name="Marca"
    )

    dealer_id = models.IntegerField(
        verbose_name="ID del Concesionario",
        null=True,
        blank=True
    )
    name = models.CharField(max_length=100, verbose_name="Nombre")
    type = models.CharField(
        max_length=20,
        choices=CarType.choices,
        default=CarType.SEDAN,
        verbose_name="Tipo"
    )
    year = models.IntegerField(
        verbose_name="Año",
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2030)
        ]
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Precio",
        null=True,
        blank=True
    )

    # Metadatos para el modelo
    class Meta:
        verbose_name = "Modelo de automóvil"
        verbose_name_plural = "Modelos de automóviles"
        ordering = ['car_make__name', 'name', 'year']

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
