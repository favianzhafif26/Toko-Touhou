from django.shortcuts import render, redirect
from main.forms import ItemEntryForm
from main.models import ItemEntry
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    item_entries = ItemEntry.objects.all()
    context = {
        'identity':{
                'nama': 'Nama: Favian Zhafif Rizqullah Permana',
                'npm': 'NPM: 2306274996',
                'kelas': 'Kelas: PBP-D',
        },
        'products':     
                {
                'item_entries': item_entries
            }
    }

    return render(request, "main.html", context)

def create_item_entry(request):
    form = ItemEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_item_entry.html", context)

def show_xml(request):
    data = ItemEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ItemEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ItemEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ItemEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")