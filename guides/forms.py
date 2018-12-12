from django import forms

from .models import Guide


class GuideForm(forms.ModelForm):
    class Meta:
        model = Guide
        fields = (
            'ascendancy',
            'author',
            'character_class',
            'content',
            'items',
            'patch_version',
            'primary_skill',
            'tags',
            'title')
