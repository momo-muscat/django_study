from django import forms


class ModelTestForm(forms.Form):
    denno = forms.CharField(label="伝票番号", max_length=14)

