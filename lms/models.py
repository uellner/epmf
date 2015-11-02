# -*- coding: utf-8 -*-

from django.db import models
from django.utils.timezone import datetime


class Course(models.Model):
    u"""
        Classe que representa as informações de um curso.
    """
    title = models.CharField(max_length=155)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    summary = models.TextField(max_length=500)
    description = models.TextField('course description')
    logo = models.ImageField()

    def __str__(self):
        return self.title


class Unit(models.Model):
    u"""
        Classe que representa as informações de uma unidade de curso.
    """
    title = models.CharField(max_length=155)
    summary = models.TextField(max_length=500)
    content = models.TextField('unit content')
    course = models.ForeignKey(Course)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    u"""
        Classe que representa as informações de uma lição de unidade.
    """
    title = models.CharField(max_length=155)
    main_type = models.CharField(max_length=155)
    content = models.TextField('lesson content')
    unit = models.ForeignKey(Unit)

    def __str__(self):
        return self.title
