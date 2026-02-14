from django.shortcuts import render
from django.db.models import OuterRef, Subquery, Q
from django.utils import timezone

from apl.models.models import HaiinfoTbl, KiriTbl
from .forms import ModelTestForm

searched = False

def ModelTestView(request):
    template_name = "model_test/index.html"

    form = ModelTestForm()
    ctx = {}
    ctx["form"] = form

    if request.POST:
        form = ModelTestForm(request.POST)
        ctx["form"] = form

        if form.is_valid():
            denno = form.cleaned_data["denno"]
            order_date_from = form.cleaned_data["order_date_from"]
            order_date_to = form.cleaned_data["order_date_to"]
            
            # 時刻を付加
            if order_date_from:
                # order_date_from = str(order_date_from) + " 00:00:00.000"
                order_date_from = str(order_date_from) + " 5:34:05.593"
            if order_date_to:
                # order_date_to = str(order_date_to) + " 23:59:59.999"
                order_date_to = str(order_date_to) + " 5:34:05.593"
            
            print("order_date_from: ", order_date_from)
            print("order_date_to: ", order_date_to)

            qs = HaiinfoTbl.objects.filter(
                Q(order_date__gte=order_date_from) & Q(order_date__lte=order_date_to)
            )

            # den_type_subquery = HaiinfoTbl.objects.filter(
            #     denno=OuterRef("denno")
            # ).values("den_type")[:1]
            # s_den_type_subquery = HaiinfoTbl.objects.filter(
            #     denno=OuterRef("s_denno")
            # ).values("den_type")[:1]

            # qs = KiriTbl.objects.filter(Q(denno=denno) | Q(s_denno=denno)).values("denno", "s_denno")[:1]

            # if not qs.exists():
            #     return render(request, template_name, ctx)
            # else:
            #     qs = KiriTbl.objects.filter(denno=qs[0]["denno"]).annotate(
            #         den_type=Subquery(den_type_subquery),
            #         s_den_type=Subquery(s_den_type_subquery),
            #     ).values("denno", "den_type", "s_denno", "s_den_type").order_by("s_denno")

            for item in qs:
                print(item.denno, timezone.localtime(item.order_date))

    return render(request, template_name, ctx)
