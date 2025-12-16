from django import forms
from . models import Todo
# to add textinput
from django.forms import TextInput


class Todoforms(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title']
        # __all__

        widgets={
            'title':TextInput(attrs={
                'type' :"text",
                'class':"form-control",
                'placeholder': "Enter your Todos",
                })
        }