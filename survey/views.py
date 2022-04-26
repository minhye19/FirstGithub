from django.shortcuts import render
from django.http import HttpResponse
from survey.models import Survey

def q1(request):
    return render(request, 'survey/q1.html')

def q2(request):
    select = request.GET.get('whereBetter')
    context = {
        'select': select,
    }
    return render(request, 'survey/q2.html', context)

def SVlist(request):
    print("list 모듈동작!")
    survey = Survey.objects.filter(status='y').order_by('-survey_idx')[0]
    return render(request, "survey/list.html", {'survey': survey})
