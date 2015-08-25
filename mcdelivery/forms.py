from .models import Order
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class OrderForm(forms.ModelForm):
    class Meta: 
        model = Order
        exclude = ('user',)
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Save', 'Save', css_class='btn-primary'))