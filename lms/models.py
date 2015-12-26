# -*- coding: utf-8 -*-

from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User


class Course(models.Model):
    u"""
        Classe que representa as informações de um curso.
    """
    title = models.CharField(max_length=155)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    summary = models.TextField(max_length=500)
    description = models.TextField('course description')
    logo = models.ImageField(upload_to='courses/%Y/%m/%d', null=True)

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
    main_image = models.ImageField(upload_to='units/%Y/%m/%d', null=True)

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
    main_image = models.ImageField(upload_to='lessons/%Y/%m/%d', null=True)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    u"""
        Classe que representa as informações de um perfil de usuario
    """
    cpf = models.CharField(max_length=30, unique=True)
    main_phone = models.CharField(max_length=50)
    avatar = models.ImageField("Imagem perfil", upload_to="images/users", blank=True, null=True)
    user = models.OneToOneField(User, related_name="profile")

    def __str__(self):
        return self.cpf
