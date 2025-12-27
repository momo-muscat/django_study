from django.contrib import admin
from .models import IntTest, CharTest, DateTest, FieldTest, NameMst


# 整数テスト
admin.site.register(IntTest)

# 文字列テスト
admin.site.register(CharTest)

# 日付テスト
admin.site.register(DateTest)


# フィールドテスト
class FieldTestAdmin(admin.ModelAdmin):
    list_display =  [field.name for field in FieldTest._meta.fields]

admin.site.register(FieldTest, FieldTestAdmin)


# 名称マスタ
class NameMstAdmin(admin.ModelAdmin):
    list_display =  [field.name for field in NameMst._meta.fields]

admin.site.register(NameMst, NameMstAdmin)

