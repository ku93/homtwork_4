from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField, forms

from catalog.models import Product, Category

FORBIDDEN_WORDS = [
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

VALID_IMAGE_FORMATS = ['image/jpeg', 'image/png']
MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 5 MB

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
        exclude = ("views_counter", "owner",)

    def clean_name(self):
        name = self.cleaned_data['name']
        if any(word.lower() in name.lower() for word in FORBIDDEN_WORDS):
            raise ValidationError('Поле содержит запрещённые слова.')
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        if any(word.lower() in description.lower() for word in FORBIDDEN_WORDS):
            raise ValidationError('Поле содержит запрещённые слова.')
        return description

    def clean_image(self):
        image = self.cleaned_data['image']

        if hasattr(image, 'content_type') and image.content_type not in VALID_IMAGE_FORMATS:
            raise forms.ValidationError(f'Допустимые форматы изображений: {", ".join(VALID_IMAGE_FORMATS)}.')

        if image.size > MAX_IMAGE_SIZE:
            raise forms.ValidationError(f'Максимальный размер файла - {MAX_IMAGE_SIZE / 1024 / 1024:.2f} МБ.')

        return image

class ProductModeratorForm(StyledFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ("is_published",)

class CategoryForm(StyledFormMixin, ModelForm):
    class Meta:
        model = Category
        exclude = ("views_counter",)