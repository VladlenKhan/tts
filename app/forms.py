from django import forms
from .models import Application
from django.utils.translation import gettext_lazy as _

class ApplicationForm(forms.ModelForm):
    name = forms.CharField(label=_("ФИО"), max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    phone_number = forms.CharField(label=_("Номер телефона"), max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    Comment = forms.CharField(label=_("Ваше сообщение"), widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 30, 'rows': 10}), required=False)


    class Meta:
        model = Application
        fields = ['name', 'email', 'phone_number', 'Comment']