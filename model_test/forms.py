from django import forms

class ModelTestForm(forms.Form):
    cd = forms.IntegerField(label="コード")
    nm = forms.CharField(label="名称")
