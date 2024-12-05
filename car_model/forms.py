from django import forms
from .models import Brand, CarModel, Comment

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'description', 'image']

class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ['name', 'brand', 'quantity', 'price', 'description', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment_text']