from django.shortcuts import render
from django.http import HttpResponse

def q1(request):
    return render(request, 'question/q1.html')

def q2(request):
    select = request.GET.get('whereBetter')
    context = {
        'select': select,
    }
    return render(request, 'question/q2.html', context)