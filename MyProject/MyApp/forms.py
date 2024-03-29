from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    desc =  forms.CharField(max_length=200)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity = forms.IntegerField()
    photo = forms.ImageField(required = False)

