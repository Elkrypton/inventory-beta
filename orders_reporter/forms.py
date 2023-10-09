from django import forms
import pyqrcode
from django import forms
from .models import Manufacturer, Note, SearchProduct
class ManufacturerForm(forms.ModelForm):

    class Meta:
        model = Manufacturer
        fields = ['item', 'quantity', 'date_of_production', 'sku', 'location']
        widgets = {
            'item': forms.TextInput(attrs={'size':'40', 'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'size':'40','class': 'form-control'}),
            'date_of_production': forms.widgets.DateInput(attrs={'type': 'date'}),

            'sku': forms.TextInput(attrs={'size':'40','class': 'form-control'}),
            'location': forms.TextInput(attrs={'size':'40','class': 'form-control'})}


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ['name','feedback']
        widgets = {
        'name':forms.TextInput(attrs={'size':'40', 'class': 'form-control'}),
        'feedback': forms.Textarea()}


class SearchForm(forms.ModelForm):
    class Meta:
        model = SearchProduct
        fields = ['query']
        widgets = {
        'query':forms.TextInput(attrs={'size':'40', 'class': 'form-control'})}
