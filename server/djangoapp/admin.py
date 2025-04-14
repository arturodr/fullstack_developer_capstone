from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1
    fields = ('name', 'type', 'year', 'dealer_id')


# CarMakeAdmin class
@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'country_of_origin')
    search_fields = ('name', 'description', 'country_of_origin')
    inlines = [CarModelInline]


# CarModelAdmin class
@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'dealer_id', 'price')
    search_fields = ('name', 'car_make__name', 'dealer_id')
    autocomplete_fields = ['car_make']
    fieldsets = (
        ('Información básica', {
            'fields': ('car_make', 'name', 'type', 'year')
        }),
        ('Información de concesionario', {
            'fields': ('dealer_id',)
        }),
        ('Especificaciones técnicas', {
            'fields': ('price',),
            'classes': ('collapse',)
        }),
    )
