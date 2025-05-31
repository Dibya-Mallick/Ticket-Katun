from django import forms
from .models import Details,ContactInfo,ReserveInfo

class DetailsForm(forms.ModelForm):
    class Meta:
        model=Details
        fields=['Boarding','Destination','Date','Coach']
        widgets = {'Boarding': forms.TextInput(attrs={'class': 'my-custom-class'}),
                   'Destination': forms.TextInput(attrs={'class': 'my-custom-class'}),
                   'Date': forms.TextInput(attrs={'class': 'my-custom-class','placeholder':'YYYY--MM--DD'}),
                   'Coach': forms.Select(attrs={'class': 'my-custom-class'})
        }

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model=ContactInfo
        fields=['name','phone','city','email','message']
        widgets = {'name': forms.TextInput(attrs={'class': 'my-custom-class'}),
                   'phone': forms.TextInput(attrs={'class': 'my-custom-class','placeholder':'01xxxxxxxxx'}),
                   'city': forms.TextInput(attrs={'class': 'my-custom-class'}),
                   'email': forms.TextInput(attrs={'class': 'my-custom-class'}),
                   'message': forms.TextInput(attrs={'class': 'my-custom-class1'})
        }

class ReserveInfoForm(forms.ModelForm):
    class Meta:
        model=ReserveInfo
        fields=['journey_date','return_date','boarding','destination','pref_bus','no_of_bus','no_of_seat','name','phone','address','email']
        widgets={'journey_date': forms.TextInput(attrs={'class': 'my-custom-class'}),
                 'return_date': forms.TextInput(attrs={'class': 'my-custom-class'}),
                 'boarding': forms.TextInput(attrs={'class': 'my-custom-class'}),
                 'destination': forms.TextInput(attrs={'class': 'my-custom-class'}),
                 'pref_bus': forms.TextInput(attrs={'class': 'my-custom-class'}),  
                 'no_of_bus': forms.Select(attrs={'class': 'form-select'}),
                 'no_of_seat': forms.Select(attrs={'class': 'form-select'}),
                 'name': forms.TextInput(attrs={'class': 'my-custom-class'}),
                 'phone': forms.TextInput(attrs={'class': 'my-custom-class','placeholder':'01xxxxxxxxx'}),
                 'address': forms.TextInput(attrs={'class': 'my-custom-class'}),
                 'email': forms.TextInput(attrs={'class': 'my-custom-class'})              
        }