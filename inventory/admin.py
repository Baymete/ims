from django.contrib import admin

from .models import Item, Personnel


class ItemAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Item)
admin.site.register(Personnel)
    
