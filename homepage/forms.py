from django import forms
from django.forms import ModelForm

from .models import *

  
class BookingForm (forms.Form):
    T1 = '13:00'
    T2 = '13:30'
    T3 = '14:00'
    T4 = '14:30'
    T5 = '15:00'
    T6 = '15:30'
    T7 = '20:00'
    T8 = '20:30'
    T9 = '21:00'
    T10 = '21:30'
    T11 = '22:00'
    T12 = '22:30'
    T13 = '23:00'    
    CHOICES = (
    (T1,'13:00'),
    (T2,'13:30'),
    (T3,'14:00'),
    (T4,'14:30'),
    (T5,'15:00'),
    (T6 , '15:30'),
    (T7 , '20:00'),
    (T8 , '20:30'),
    (T9 , '21:00'),
    (T10 , '21:30'),
    (T11 , '22:00'),
    (T12 , '22:30'),
    (T13 , '23:00'),
    )
    date = forms.DateField(label='Date', widget = forms.DateInput(attrs={'class':'form-control','type':'date'}))
    pax = forms.IntegerField(label='Personas', widget = forms.NumberInput(attrs={'class':'form-control', 'type':'number', 'value':'2', 'min':'1', 'max':'20'}))
    hour = forms.ChoiceField(choices= CHOICES, widget = forms.Select(attrs={'class': 'form-control'}))
    comment = forms.CharField(label='Nota', widget=forms.Textarea(attrs={'class':'form-control','rows':'2'}))
    customer = forms.CharField(label='Nombre', max_length=200, widget = forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(label='Telefono', max_length=20, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'ej: +34627775591','pattern':'^\+?1?\d{8,15}$'}))
    email = forms.CharField(label='Email', max_length=200, widget = forms.TextInput(attrs={'class':'form-control'}))

class ItemForm(ModelForm):
    class Meta:
        DISPONIBLE = True
        NO_DISPONIBLE = False
        
        av = [(DISPONIBLE,'DISPONIBLE'),(NO_DISPONIBLE,'NO DISPONIBLE')]        
        model = Item
        fields = ['name', 'description', 'price', 'available']
        
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.TextInput(attrs={'class':'form-control', 'required':False }),
            'price' : forms.TextInput(attrs={'class':'form-control'}),
            'available' : forms.Select(choices= av, attrs={'class':'form-control'}),
            
        }
        
class SearchForm(forms.Form):
    ITEMS = [(choice.pk, choice.name) for choice in Item.objects.all()]

    item = forms.ChoiceField(choices= ITEMS, widget = forms.Select(attrs={'class': 'form-select'}))