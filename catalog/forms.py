from django import forms
from django.forms import BooleanField

from catalog.models import Product, Version


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(FormStyleMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category']

    @staticmethod
    def validate_bad_words(field):
        forbidden_words = [
            'казино', 'криптовалюта', 'крипта', 'биржа',
            'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
        ]
        for word in forbidden_words:
            if word in field.lower():
                raise forms.ValidationError('Нельзя использовать запрещенные слова.')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        self.validate_bad_words(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        self.validate_bad_words(description)
        return description


class VersionForm(FormStyleMixin, forms.ModelForm):
    name_version = forms.CharField(label="Название")

    class Meta:
        model = Version
        fields = ['name_version', 'number']
