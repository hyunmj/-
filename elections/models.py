# -*- coding: utf-8 -*-
#클래스 정의, 데이터 관리 -> 모델(데이터)

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=10)
    introduction = models.TextField()
    area = models.CharField(max_length=15)
    party_number = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Poll(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    area = models.CharField(max_length = 15)


class Choice(models.Model):
    #어느 투표에 대한 결과?
    poll = models.ForeignKey(Poll, on_delete = models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete = models.CASCADE)
    votes = models.IntegerField(default = 0)
