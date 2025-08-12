from django import forms
from defects.models import Defect

class DefectEditForm(forms.ModelForm):
    defectid = forms.CharField(max_length=100,disabled=True)
    defect_name = forms.CharField(max_length=200,disabled=True)
    class Meta:
        model = Defect
        fields = ['defectid', 'defect_name', 'assignedby', 'assignedto', 'description','defect_edit', 'defect_status', 'priority']


class Adddefect(forms.ModelForm):
    class Meta:
        model = Defect
        fields = '__all__'


class FilterDefectForm(forms.ModelForm):
    class Meta:
        model = Defect
        fields = ['assignedto']