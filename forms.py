from django import forms

class ProductInsertForm(forms.Form):
    product_id=forms.IntegerField(
        label="enter product id",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'product id'
            }
        )
    )
    product_type=forms.CharField(
        label="enter product type",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'product type'
            }
        )
    )
    product_cost=forms.IntegerField(
        label="enter cost of product",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'product cost'
            }
        )
    )
    product_class=forms.CharField(
        label="enter product class",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'product class'
            }
        )
    )
    product_color=forms.CharField(
        label="enter product color",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'product color'
            }
        )
    )
    brand_name=forms.CharField(
        label="enter product brand",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'product brand'
            }
        )
    )
    organisation_mobile_no=forms.IntegerField(
        label="enter organisation mobile no:",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'organisation mobile no'
            }
        )
    )
    organisation_email=forms.EmailField(
        label="enter organisation email id:",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'organisation email id'
            }
        )
    )
class ProductUpdateForm(forms.Form):
    product_id=forms.IntegerField(
    label="enter product id",
    widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'product id',
            }
         )
    )
    product_cost=forms.IntegerField(
        label="enter new cost of product",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'product new cost'
            }
        )
    )
class ProductDeleteForm(forms.Form):
    product_id = forms.IntegerField(
        label="enter product id",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product id should be deleated',
            }
        )
    )
