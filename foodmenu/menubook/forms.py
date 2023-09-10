from django import forms

from .models import Items


class Itemform(forms.ModelForm):
    class Meta:
        model = Items
        fields = ["item_name", "item_desc", "price", "item_image"]
