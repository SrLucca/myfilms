from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    watched_date = forms.DateField(
        label="Data assistida",
        widget=forms.widgets.Input(attrs={'type':'date'}),
        required=False
    )
    class Meta:
        model = Movie
        fields = ['title', 'watched_date', 'gender','wish_list']

        labels = {
            'title': 'Título',
            'watched_date': 'Data assistida',
            'gender': 'Gênero',
            'wish_list': 'Quero Assistir',
        }