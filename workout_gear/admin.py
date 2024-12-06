from django.contrib import admin
from .models import GearCategory, GearItem


# Admin configuration for GearCategory
@admin.register(GearCategory)
class GearCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name')
    search_fields = ('name', 'friendly_name')


# Admin configuration for GearItem
@admin.register(GearItem)
class GearItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'cost', 'stock_quantity', 'highlight')
    list_filter = ('category', 'highlight')
    search_fields = ('name', 'category__name', 'material_type')
    ordering = ('-created_on',)
