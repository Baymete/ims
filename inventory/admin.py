from django.contrib import admin
from inventory.forms import UsersForm
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Item, Personnel, ItemType, ItemManufacturer, ItemModel, \
    OperatingSystem, StorageCapacity, MemoryCapacity, Processor, Supplier, \
    ItemHistory


class ItemAdmin(admin.ModelAdmin):
    
    fieldsets = (
         (None, {'fields': ('serial_number', 'item_number', 'asset_number', 'current_owner')}),
         ('Item Details', {'fields': ('item_type','item_manufacturer', 'item_model', 
                                      'operating_system', 'storage_capacity', 'memory_capacity',
                                      'processor', 'supplier'),
                           'classes': ('collapse',)}),
         ('Invoice details', {'fields': ('invoice_date', 'invoice_number', 'po_number'),
                              'classes': ('collapse',)}),
         ('Warranty', {'fields':('warranty_status', 'warranty_until'),
                       'classes': ('collapse',)})
         )
    
    list_display = ('serial_number', 'entry_date', 'current_owner', 'notes')
    list_filter = ['current_owner', 'entry_date', 'item_type', 'item_manufacturer',
                   'item_model', 'operating_system', 'storage_capacity', 'memory_capacity',
                   'processor', 'supplier' ]
    search_fields = ['serial_number', 'item_number', 'asset_number', 'current_owner__username']
    date_hierarchy = 'entry_date'
    readonly_fields = ('current_owner',)
    
    
    actions = ['make_warranty', 'remove_warranty', 'route_to_user']
    
#     def save_model(self, request, obj, form, change):
#         obj.user = request.user
#         obj.save()
        
    def make_warranty(modeladmin, request, queryset):
        queryset.update(warranty_status=True)
    make_warranty.short_description = "Make warranty"
    
    def remove_warranty(modeladmin, request, queryset):
        queryset.update(warranty_status=False)
    
    def route_to_user(self, request, queryset):
        form = None
        if 'apply' in request.POST:
            form = UsersForm(request.POST)
            if form.is_valid():
                user = form.cleaned_data['users_form']
                for item in queryset:
                    item.current_owner=user
                    item.save()
                self.message_user(request, "Item routed to %s" %(user))
                return HttpResponseRedirect(request.get_full_path())
        if not form:
            user_list = User.objects.all()
            form = UsersForm(initial={'_selected_action': queryset.values_list('id', flat=True)})
        return render(request, 'users.html', {'query':queryset,
                                                 'form': form})

admin.site.register(Item, ItemAdmin)
# admin.site.register(Personnel)
# admin.site.register(ItemType)
# admin.site.register(ItemManufacturer)
# admin.site.register(ItemModel)
# admin.site.register(OperatingSystem)
# admin.site.register(StorageCapacity)
# admin.site.register(MemoryCapacity)
# admin.site.register(Processor)
# admin.site.register(Supplier)
admin.site.register(ItemHistory)
