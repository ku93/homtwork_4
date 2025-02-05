from django.forms import ModelForm, BooleanField

from blog.models import BlogPost

class StyledFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"

class BlogPostForm(StyledFormMixin, ModelForm):
    class Meta:
        model = BlogPost
        exclude = ("views_counter",)