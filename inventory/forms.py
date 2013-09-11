from django import forms
from django.contrib.auth.models import User

class UsersForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    users_form = forms.ModelChoiceField(queryset=User.objects.all())
    

class ItemForm(forms.ModelForm):
    def clean(self):
        if self.errors.has_key('current_owner') and self.has_changed():
            del self.errors['current_owner']
        return self.cleaned_data