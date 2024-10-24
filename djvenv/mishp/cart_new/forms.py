from django import forms
from .models import Cart_Items

class CartAddProductForm(forms.ModelForm):

    class Meta:    #  в мета классе указываем на основе чего будет создана модельная форма
        model = Cart_Items    # на основе модели CartItem
        fields = ['quantity']   # и будет содержать поле этой модели 'quantity'