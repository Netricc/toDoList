from django import forms
from .models import List, Category, Task


class CreateListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ['name', 'description', 'category']


class CreateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'complete']
