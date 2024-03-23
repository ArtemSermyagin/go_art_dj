from django import forms
from catalog.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category']

    def clean_name(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        name = self.cleaned_data.get('name')
        for word in forbidden_words:
            if word in name.lower():
                raise forms.ValidationError('Нельзя использовать запрещенные слова в названии продукта.')
        return name

    def clean_description(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        description = self.cleaned_data.get('description')
        for word in forbidden_words:
            if word in description.lower():
                raise forms.ValidationError('Нельзя использовать запрещенные слова в описании продукта.')
        return description