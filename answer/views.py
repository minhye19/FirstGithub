from django.shortcuts import render
from django.http import HttpResponse

def a1(request):
    select = request.GET.get('whereBetter')
    context = {
        'select': select,
    }
    return render(request, 'answer/a1.html', context)

def a2(request):
    select = request.GET.get('whereBetter')
    context = {
        'select': select,
    }
    return render(request, 'answer/a2.html', context)
