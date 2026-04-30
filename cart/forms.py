from django import forms
from .models import CartItem


class AddToCartForm(forms.Form):
    size_id = forms.IntegerField(min_value=1, initial=1)

    def __init__(self, *args, product=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.product = product

        if product:
            sizes = product.product_size.filter(stock__gt=0)  # было product_sizes — неправильное имя
            if sizes.exists():
                self.fields['size_id'] = forms.ChoiceField(
                    choices=[(ps.id, ps.size.name) for ps in sizes],
                    required=True,
                    initial=sizes.first().id
                )
    

class UpdateCartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.isinstance and self.instance.product_size:
            self.field['quantity'].validators.append(
                forms.validators.MaxValueValidaror(self.instance.product_size.stock)    
            )
