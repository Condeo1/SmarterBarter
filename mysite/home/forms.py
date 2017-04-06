import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
 
class RegistrationForm(forms.Form):
 
    id_userName = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    id_password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    id_password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
    firstName = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("First Name"))
    lastName = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Last Name"))
    zipCode = forms.IntegerField(widget=forms.NumberInput(attrs=dict(required=True, max_length=5)), label=_("Zip Code"))
    bio = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=1500)), label=_("Bio"))
    serviceID = forms.CharField(widget=forms.CheckboxSelectMultiple(attrs=dict(required=True, max_length=100)), label=_("Services"))
    #needsID = forms.CharField(widget=forms.CheckboxSelectMultiple(attrs=dict(required=True, max_length=100)), label=_("Needs"))
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
        
class HomeForm(forms.Form):

    needsID = forms.CharField(widget=forms.CheckboxSelectMultiple(attrs=dict(required=True, max_length=100)), label=_("Needs"))