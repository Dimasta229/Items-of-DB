from .models import Item
from django.shortcuts import render

def index(request):
    items = Item.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'base.html', context)