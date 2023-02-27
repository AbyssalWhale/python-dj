from django.contrib import admin
from .models import Type, Order

# To display properties in admin console for all Type records


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class OrderAdmin(admin.ModelAdmin):
    fields = ('title', 'quantity', 'delivery_address', 'date_delivery', 'type')
    list_display = ('title', 'quantity', 'delivery_address', 'date_delivery')


# Register your models here.
admin.site.register(Type, GenreAdmin)
admin.site.register(Order, OrderAdmin)
