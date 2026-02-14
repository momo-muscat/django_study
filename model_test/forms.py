from django import forms


class ModelTestForm(forms.Form):
    denno = forms.CharField(label="伝票番号", max_length=14)
    order_date_from = forms.DateField(label="注文日 (開始)", required=False, input_formats=['%Y%m%d'])
    order_date_to = forms.DateField(label="注文日 (終了)", required=False, input_formats=['%Y%m%d'])

