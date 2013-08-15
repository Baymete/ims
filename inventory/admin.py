from django.contrib import admin
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from .models import Item, Personnel


class ItemAdmin(admin.ModelAdmin):
    actions = ['make_warranty', 'remove_warranty', 'route_to_user']
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
        
    def make_warranty(modeladmin, request, queryset):
        queryset.update(warranty_status=True)
    make_warranty.short_description = "Make warranty"
    
    def remove_warranty(modeladmin, request, queryset):
        queryset.update(warranty_status=False)
    
    def route_to_user(self, request, queryset):
        return render_to_response('route.html', {'query':queryset})


admin.site.register(Item, ItemAdmin)
admin.site.register(Personnel)
    
