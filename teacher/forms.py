from django import forms

from .models import TeacherDb


class FormTeacher(forms.ModelForm):
    class Meta:
        model = TeacherDb
        fields = ['name', 'email', 'experience_years', 'subject']

    def clean_grade(self):
        experience_years = self.cleaned_data['experience_years']
        if experience_years > 0:
            return experience_years
        else:
            raise forms.ValidationError(
                "0 dan katta bo'lishi kerak")
