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
from .models import Choice

from django.http import Http404
from django.shortcuts import get_object_or_404
"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_question_list': latest_question_list, }

    return render( request, 'polls/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render (request, 'polls/detail.html', {'question':question,} )
"""
from django.views import generic

from django.utils import timezone
class IndexView(generic.ListView):
	"""docstring for IndexView
	generic.ListView: 显示一个对象列表
	"""
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	"""
	def __init__(self, arg):
		super(IndexView, self).__init__()
		self.arg = arg
	"""
	def get_queryset(self):
		"""Return the last five published questions.
		not including those set to be published in the future
		"""
		return Question.objects.filter(
			pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
	"""docstring for DetailView
	  generic.DetailView: 显示一个特定类型对象的详细信息页面
	  DetailView 期望从 URL 中捕获名为 ‘pk’ 的主键值， 
	所以我们为通用视图把 question_id 改成 pk
	"""
	model = Question
	template_name = 'polls/detail.html'
	"""
	def __init__(self, arg):
		super(DetailView, self).__init__()
		self.arg = arg
	"""
	def get_queryset(self):
		"""
		Excludes any questions that aren't published yet
		-[o] 关于 pub_date__lte=timezone.now() 是怎么工作的还不清楚
		"""
		return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
	"""docstring for ResutlsView"""
	model = Question
	template_name = 'polls/results.html'
	"""
	def __init__(self, arg):
		super(DetailView, self).__init__()
		self.arg = arg
	"""

from django.http import HttpResponseRedirect
from django.urls import reverse
def vote(request, question_id):
	question = get_object_or_404( Question, pk=question_id )
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form
		return render(request, 'polls/detail.html', 
				{ 'question':question, 
				'error_message':"You didn't select a choice." })
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(
				reverse('polls:results', args=(question.id,)))


def results(request, question_id):
	question = get_object_or_404( Question, pk=question_id )
	return render( request, 'polls/results.html', {'question':question} )
