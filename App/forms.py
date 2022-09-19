from django import forms

class MyForm(forms.Form):
    Name = forms.CharField(max_length=25)
    Email = forms.CharField(widget= forms.EmailInput)
    Password = forms.CharField(widget= forms.PasswordInput)