from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock', 'category', 'sale', 'image_tag') 

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.image.url)
        return "No Image"

    image_tag.short_description = 'Image'
    
admin.site.register(Product, ProductAdmin)