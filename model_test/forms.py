from django import forms


class ReadonlyFieldMixin:
    def __init__(self, *args, readonly=False, **kwargs):
        self.readonly = bool(readonly)
        super().__init__(*args, **kwargs)

    def set_readonly(self, readonly):
        self.readonly = bool(readonly)


class ReadonlyCharField(ReadonlyFieldMixin, forms.CharField):
    pass


class ReadonlyDateField(ReadonlyFieldMixin, forms.DateField):
    pass


class ModelTestForm(forms.Form):
    denno = ReadonlyCharField(label="伝票番号", max_length=14)
    order_date_from = ReadonlyDateField(label="注文日 (開始)", required=False, input_formats=["%Y%m%d"])
    order_date_to = ReadonlyDateField(label="注文日 (終了)", required=False, input_formats=["%Y%m%d"])
    test1 = ReadonlyCharField(label="テスト1", max_length=14)
    test2 = ReadonlyCharField(label="テスト2", max_length=14)

    def set_readonly(self, field_name, readonly):
        self.fields[field_name].set_readonly(readonly)

