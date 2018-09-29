from django.db import models

# Create your models here.
class Question(models.Model):
	"""问题模型
	
	包含了： 1. 问题描述；	2. 发布日期
	
	Extends:
		models.Model
	
	Variables:
		question_test {string} -- 问题描述
		pub_date {date} -- 发布日期
	"""
	question_text = models.CharField( max_length=200 )
	pub_date      = models.DateTimeField('date published')




class Choice(models.Model):
	"""choice 选择模型
	包含了： 1. 选项描述； 2. 当前的票数
	"""
	question    = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes		= models.IntegerField(default=0) 

	def __init__(self, arg=None):
		self.arg = arg
		

