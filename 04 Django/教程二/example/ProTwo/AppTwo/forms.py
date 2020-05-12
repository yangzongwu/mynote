from django import forms
from django.core import validators
from AppTwo.models import User

class FormName(forms.ModelForm):
    
    class Meta():
        model=User
        fields = "__all__"


'''
class FormName(forms.Form):
    fistname=forms.CharField()
    lastname=forms.CharField()
    email=forms.EmailField()
    verify_email=forms.EmailField(label="input your email again")


    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['email']
        vmail=all_clean_data['verify_email']
        if email!=vmail:
            raise forms.ValidationError("Email do not match")
'''
