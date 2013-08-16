from django.contrib import admin
from inventory.forms import UsersForm
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, render
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
        if request.method == 'POST':
            form = UsersForm(request.POST)
            if form.is_valid():
                user = form.cleaned_data['users_form']
                for item in queryset:
                    item.current_owner=user
                    item.save()
                self.message_user(request, "Item routed")
                return HttpResponseRedirect(request.get_full_path())
        else:
            user_list = User.objects.all()
            form = UsersForm()
        return render(request, 'users.html', {'query':queryset,
                                                 'form': form})


admin.site.register(Item, ItemAdmin)
admin.site.register(Personnel)

