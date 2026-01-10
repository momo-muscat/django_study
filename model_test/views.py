from django.shortcuts import render
from .models import NameMst
from .forms import ModelTestForm

seached = False

def ModelTestView(request):
    template_name = "model_test/index.html"

    form = ModelTestForm()
    ctx = {}
    ctx["form"] = form

    if request.GET:
        # obj = {}
        # qs = NameMst.objects.all()
        # obj["object_list"] = qs

        seached = True

    if request.POST:
        pass

    return render(request, template_name, ctx)
