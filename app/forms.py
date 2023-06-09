from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    name = forms.CharField(label="ФИО", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    phone_number = forms.CharField(label="Номер телефона", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    Comment = forms.CharField(label="Ваше сообщение", widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 30, 'rows': 10}), required=False)


    class Meta:
        model = Application
        fields = ['name', 'email', 'phone_number', 'Comment']