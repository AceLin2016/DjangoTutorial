from django.db import models

# Create your models here.

from .AttrDisplay import AttrDisplay
from django.utils import timezone
import datetime
class Question(models.Model, AttrDisplay):
	"""问题模型
	
	包含了： 1. 问题描述；	2. 发布日期
	
	Extends:
		models.Model
	
	Variables:
		question_text {string} -- 问题描述
		pub_date {date} -- 发布日期
	"""
	question_text = models.CharField( max_length=200 )
	pub_date      = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model, AttrDisplay):
	"""choice 选择模型
	包含了： 1. 选项描述； 2. 当前的票数
	"""
	question    = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes		= models.IntegerField(default=0) 

	# def __init__(self, arg=None):
	# 	self.arg = arg
		
	def __str__(self):
		return self.choice_text

