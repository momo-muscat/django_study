from django.shortcuts import render
from django.db.models import OuterRef, Subquery, Q

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

            den_type_subquery = HaiinfoTbl.objects.filter(
                denno=OuterRef("denno")
            ).values("den_type")[:1]
            s_den_type_subquery = HaiinfoTbl.objects.filter(
                denno=OuterRef("s_denno")
            ).values("den_type")[:1]

            qs = KiriTbl.objects.filter(Q(denno=denno) | Q(s_denno=denno)).values("denno", "s_denno")[:1]

            if not qs.exists():
                return render(request, template_name, ctx)
            else:
                qs = KiriTbl.objects.filter(denno=qs[0]["denno"]).annotate(
                    den_type=Subquery(den_type_subquery),
                    s_den_type=Subquery(s_den_type_subquery),
                ).values("denno", "den_type", "s_denno", "s_den_type").order_by("s_denno")

            for item in qs:
                print(item)

    return render(request, template_name, ctx)
