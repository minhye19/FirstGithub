from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

from survey.models import Survey, Answer

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

def home(request):
    print("list 모듈 동작!")
    # filter 조건절에 해당
    # [0] 레코드중에서 첫번째 요청
    # select * from survey_survey where status='y' => row 10
    # 최신 데이터 1개만 추출 / 내림차순 : order by('-xx')[index]
    survey = Survey.objects.filter(status='y').order_by('-survey_idx')[0]

    return render(request, "survey/list.html", {'survey': survey})

@csrf_protect
def save_survey(request):
    # 문제 번호와 응답번호를 Answer 객체에 저장한다.
    survey_idx = request.POST["survey_idx"]
    print("Type : ", type(survey_idx))
    # survey_survey primary key -> 1:n 질문에 대한 답변의 값(survey)
    # num :선택한 설문의 항목 번호
    dto = Answer(survey_idx=int(request.POST["survey_idx"]), num=request.POST["num"])
    # insert query 가 호출
    dto.save()

    return render(request, "survey/success.html", {'survey_idx': survey_idx})

@csrf_protect
def show_result(request):
    # 문제 번호
    idx = request.GET["survey_idx"]

    # select * from survey where survey_idx=1 과 같다.
    ans = Survey.objects.get(survey_idx=idx)

    # 각 문항에 대한 값으로 리스트를 만들어 놓는다.
    answer = [ans.ans1, ans.ans2, ans.ans3, ans.ans4]

    # Survey.objects.raw("""SQL문""")
    surveyList = Survey.objects.raw("""
        SELECT survey_idx, num, count(num) sum_num FROM survey_answer
            WHERE survey_idx=%s
            GROUP BY survey_idx,num
            ORDER BY num
        """, idx)

    surveyList = zip(surveyList, answer)

    return render(request, "survey/result.html", {'surveyList': surveyList})