from django import forms
from listings.models import Band, Listing

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        # fields = '__all__'
        exclude = ('active', 'official_home_page')

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        # fields = '__all__'
        exclude = ('band', 'sold')

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(error_messages={'invalid': 'Email invalide', 'required': 'Ce champ est obligatoire'})
    message = forms.CharField(max_length=1000, error_messages={'required': 'Ce champ est obligatoire'})

