from django import forms


class ModelTestForm(forms.Form):
    denno = forms.CharField(label="伝票番号", max_length=14)
    order_date_from = forms.DateField(label="注文日 (開始)", required=False, input_formats=['%Y%m%d'])
    order_date_to = forms.DateField(label="注文日 (終了)", required=False, input_formats=['%Y%m%d'])
    test1 = forms.CharField(label="テスト1", max_length=14)
    test2 = forms.CharField(label="テスト2", max_length=14)

    def __init__(self, *args, test1_readonly=False, test2_readonly=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.test1_readonly = bool(test1_readonly)
        self.test2_readonly = bool(test2_readonly)

