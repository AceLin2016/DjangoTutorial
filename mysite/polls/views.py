from django.shortcuts import render

# Create your views here.
"""mysite/polls/views.py

该文件专注于如何创建公用界面 -- 也被称为“视图”
	* 问题索引页——展示最近的几个投票问题。                  (index)
	* 问题详情页——展示某个投票的问题和不带结果的选项列表。   (detail)
	* 问题结果页——展示某个投票的结果。                      ()
	* 投票处理器——用于响应用户为某个问题的特定选项投票的操作。 ()
"""

from django.http import HttpResponse

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_question_list': latest_question_list, }

    return render( request, 'polls/index.html', context)

from django.http import Http404
def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)

	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render (request, 'polls/detail.html', {'question':question,} )





