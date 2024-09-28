from django import forms
from .models import Recipe, RecipeSchedule

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'image', 'rating', 'date', 'is_inspiring', 'ingredients']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control recipe-textarea', 'rows': 5}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_inspiring': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control recipe-textarea', 'rows': 5}),
        }

class RecipeScheduleForm(forms.ModelForm):
    class Meta:
        model = RecipeSchedule
        fields = ['recipe', 'datetime']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['recipe'].queryset = Recipe.objects.filter(user=user)
        self.fields['datetime'].widget = forms.DateTimeInput(attrs={
            'type': 'datetime-local',
        })