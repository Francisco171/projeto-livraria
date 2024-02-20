from django import forms

from livraria.models import Livro

class LivroForm(forms.ModelForm):

    class Meta:
        model = Livro
        fields = ('nome','autor','categoria','codigo',
        'quantidade', 'valor', 'imagem', 'ano', 'descricao')

        widgets = {
            'nome': forms.TextInput(attrs={ 'class': 'form-control',
                                            'placeholder':'Redes de Computadores'}),
            'autor': forms.SelectMultiple(attrs={ 'class': 'form-control', 'placeholder': 'Nome do Autor'}),
            'categoria': forms.Select(attrs={ 'class': 'form-control', 'placeholder': 'Categoria do Livro'}),
            'codigo': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Ex. 1010101'}),
            'quantidade': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Ex. 25'}),
            'valor': forms.TextInput(attrs={ 'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={ 'class': 'form-control'}),
            'ano': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Ex.2021'}),
            'descricao': forms.Textarea(attrs={ 'class': 'form-control'}),
        }
