from django import forms
from django.urls import reverse_lazy

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']
        labels = {
            'name': 'Nombre',
            'comment': 'Comentario'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Nombre',
                    'id': 'name',
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su comentario',
                    'id': 'comment',
                }
            )
        }
