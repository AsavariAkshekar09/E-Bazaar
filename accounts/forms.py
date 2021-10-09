from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class'       : 'form-control',
    }))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class'       : 'form-control',
    }))
    class Meta:
        model =  Account
        fields = ['first_name','last_name','phone_number','email','password']


    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'James'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Smith'
        self.fields['phone_number'].widget.attrs['placeholder'] = '1234-567-890'
        self.fields['email'].widget.attrs['placeholder'] = 'yourname@gmail.com'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['confirm_password'].widget.attrs['placeholder'] = 'Repeat Password'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )
