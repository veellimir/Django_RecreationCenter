from django import forms


class SupportForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'input_auth'}))
    phone = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'input_auth'}))