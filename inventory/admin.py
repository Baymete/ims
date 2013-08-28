from django.contrib import admin
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import UsersForm
from .models import Item, Personnel, ItemType, ItemManufacturer, ItemModel, \
    OperatingSystem, StorageCapacity, MemoryCapacity, Processor, Supplier, \
    ItemHistory


class ItemForm(forms.ModelForm):
    def clean(self):
        if self.errors.has_key('current_owner') and self.has_changed():
            del self.errors['current_owner']
        return self.cleaned_data


class ItemAdmin(admin.ModelAdmin):
    form = ItemForm
    
    fieldsets = (
         (None, {'fields': ('serial_number', 'item_number', 'asset_number', 'current_owner',
                            'notes')}),
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
    
    
    actions = ['make_warranty', 'remove_warranty', 'route_to_user']

    def get_readonly_fields(self, request, obj = None):
        if obj:
            return ('current_owner,')
        else:
            return ()


    
# class ItemHistoryAdmin(admin.ModelAdmin):
#     
#     fieldsets = (
#          (None, {'fields': ('serial_number', 'item_number', 'asset_number', 'current_owner')}),
#          ('Invoice details', {'fields': ('invoice_date', 'invoice_number', 'po_number')}),
#          ('Warranty', {'fields':('warranty_status', 'warranty_until')})
#          )
#     readonly_fields = ('serial_number', 'item_number', 'asset_number', 'current_owner', 
#                        'invoice_date', 'invoice_number', 'po_number', 'warranty_status', 
#                        'warranty_until')
                                      
        
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
admin.site.register(Personnel)
admin.site.register(ItemType)
admin.site.register(ItemManufacturer)
admin.site.register(ItemModel)
admin.site.register(OperatingSystem)
admin.site.register(StorageCapacity)
admin.site.register(MemoryCapacity)
admin.site.register(Processor)
admin.site.register(Supplier)
admin.site.register(ItemHistory)
