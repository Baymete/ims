from django.contrib import admin
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render_to_response

from .models import Item, Personnel


def make_warranty(modeladmin, request, queryset):
    queryset.update(warranty_status=True)
make_warranty.short_description = "Make warranty"

def remove_warranty(modeladmin, request, queryset):
    queryset.update(warranty_status=False)


class RouteToUser(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    user = forms.ModelChoiceField(User.objects)

def route_to_user(self, request, queryset):
    form = None
    
    if 'apply' in request.POST:
        form = self.RouteToUser(request.POST)

        if form.is_valid():
            user = form.cleaned_data['user']

            count = 0
            for item in queryset:
                item.user = user
                count += 1
                
            return HttpResponseRedirect(request.get_full_path())
        
        if not form:
            form = self.RouteToUser(initial= {'_selected_action': request.POST.getList(admin.ACTION_CHECKBOX_NAME)})

    return render_to_response('admin/route_to_user.html', 
                                      {'users': queryset, 'user_form': form,})

class ItemAdmin(admin.ModelAdmin):
    actions = [make_warranty, remove_warranty, route_to_user]
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Item, ItemAdmin)
admin.site.register(Personnel)
    
