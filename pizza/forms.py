from  django import forms
from .models import Pizza,Size


class PizzaForm(forms.ModelForm):
    class Meta:
        model=Pizza
        fields = ["topping1","topping2","size"]
        labels = {"topping1":"topping1","topping2":"topping2"}
        
class MultiPizzaForm(forms.Form):
    number=forms.IntegerField(min_value=2,max_value=6)