from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Items
from .forms import Itemform
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.
def index(request):
    item_list = Items.objects.all()
    context = {
        "item_list": item_list,
    }
    return render(request, "menubook/index.html", context)


class ClassBasedIndex(ListView):
    model = Items
    template_name = "menubook/index.html"
    context_object_name = "item_list"


def details(request, item_id):
    item = Items.objects.get(pk=item_id)
    return render(
        request,
        "menubook/details.html",
        {
            "item": item,
        },
    )


class DetailClassView(DetailView):
    model = Items
    template_name = "menubook/details.html"


def add_item(request):
    item = Itemform(request.POST or None)
    print(request.POST)
    if item.is_valid():
        print("valid")
        item.save()
        return redirect("menubook:index")

    return render(request, "menubook/additem.html", {"form": item})


def update_item(request, id):
    item = Items.objects.get(id=id)
    form = Itemform(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect("menubook:index")
    return render(
        request,
        "menubook/additem.html",
        {
            "form": form,
            "item": item,
        },
    )


def delete_item(request, id):
    item = Items.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect("menubook:index")

    return render(request, "menubook/deleteItem.html", {"item": item})
