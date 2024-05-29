from django.http import HttpResponse
from django.shortcuts import render

from items.models import Item


# Create your views here.

def get_item(request, pk):
    # item = Item.objects.filter(price="Tovar")
    item = Item.objects.get(id=pk)
    return HttpResponse(f'''
    <p>{item.name}</p>
    <p>{item.description}</p>
    <p>{item.price}</p>
''')

def get_all(request, pk):
    item = Item.objects.filter(id>0)
    for i in item:
        return HttpResponse(f'''
            <p>{item.name}</p>
            <p>{item.description}</p>
            <p>{item.price}</p>
            <p>{item.created_at}</p>
''')
def delete_first(request, pk):
    item = Item.objects.get(id=pk)
    if item == 1:
        return item.delete()

