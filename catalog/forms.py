from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product, Category


class StyledFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"

class ProductForm(StyledFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ("views_counter",)

    def clean_name(self):
        name = self.cleaned_data['name']

        forbidden_words = [
            'казино',
            'криптовалюта',
            'крипта',
            'биржа',
            'дешево',
            'бесплатно',
            'обман',
            'полиция',
            'радар'
        ]

        for word in forbidden_words:
            if word.lower() in name.lower():
                raise ValidationError('Поле содержит запрещённые слова.')

        return name

    def clean_description(self):
        description = self.cleaned_data['description']

        forbidden_words = [
            'казино',
            'криптовалюта',
            'крипта',
            'биржа',
            'дешево',
            'бесплатно',
            'обман',
            'полиция',
            'радар'
        ]

        for word in forbidden_words:
            if word.lower() in description.lower():
                raise ValidationError('Поле содержит запрещённые слова.')

        return description


    def clean_purchase_price(self):
        purchase_price = self.cleaned_data["purchase_price"]
        if purchase_price < 0:
            raise ValidationError("цена продукта не может быть отрицательной")
        else:
            return purchase_price

class CategoryForm(StyledFormMixin, ModelForm):
    class Meta:
        model = Category
        exclude = ("views_counter",)