from django.contrib import admin
from .models import Place

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'place_type')
    list_editable = ('rating',)
