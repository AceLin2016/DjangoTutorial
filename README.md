# README

  通过 Django 官方 Tutorial 练习 Django

## *Overview*

[TOC]

## Contents

  N/A

## Summary

N/A

## ToDo

- [ ] 教程5 - django 的 “模块” 测试

## Note

n/a


## Change Log

### 教程2 - model & 数据库

1. 创建 models.py， 
2. 在 models.py 中创建 “数据模型”类（？） -- 数据库的表
3.  `$ python manage.py shell` 实践操作数据库 API



### 教程5 - django 的“单元”测试

创建了 `mysite/polls/test.py` 使用 `$ python manage.py test polls` 来运行测试。

```python
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTest(TestCase):
	def test_was_published_recently_with_future_question(self):
		"""
		was_published_recently() returns False for question 
		whose pub_date is in the future.
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)

```

这将暴露 Question 这个 model 的 was_published_recently() 这个函数的一个 bug ！



