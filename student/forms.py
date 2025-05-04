from django import forms

from .models import StudentDb


class FormStudent(forms.ModelForm):
    class Meta:
        model = StudentDb
        fields = ['full_name','grade','is_active']
        
    def clean_grade(self):
        grade = self.cleaned_data['grade']
        if grade >= 0 and grade <= 100:
            return grade
        else:
            raise forms.ValidationError("0 va 100 oralig'ida bo'lishi kerak ball")
        