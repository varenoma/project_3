from django import forms

from .models import FeedBack


class FormFeedBack(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ['student_name', 'message']