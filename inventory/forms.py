from django import forms
from django.contrib.auth.models import User

class UsersForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    users_form = forms.ModelChoiceField(queryset=User.objects.all())