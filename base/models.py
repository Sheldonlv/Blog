#coding:utf-8
from django.db import models
import django.utils.timezone as timezone

class essay_data(models.Model):
    Num = models.CharField(u'ID', max_length=20)
    img = models.CharField(u'img', max_length=500)
    content = models.TextField(u'内容')
    pub_time = models.DateTimeField(u'发表时间',default = timezone.now)
    up_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)
    
    def __unicode__(self):
        return self.Num

class para_data(models.Model):
    Num = models.CharField(u'ID', max_length=20)
    title = models.CharField(u'标题', max_length=30)
    img = models.CharField(u'img', max_length=500)
    writer = models.CharField(u'作者', max_length=30)
    doc_type = models.CharField(u'类型', max_length=20)
    reco = models.CharField(u'推荐', max_length=5)
    content = models.TextField(u'摘要')
    pub_time = models.DateTimeField(u'发表时间',default = timezone.now)
    up_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)
    
    def __unicode__(self):
        return self.Num

class article_data(models.Model):
    Num = models.CharField(u'ID', max_length=20)
    content = models.TextField(u'内容')
    viewed = models.CharField(u'阅读次数', max_length=20)
    
    def __unicode__(self):
        return self.Num

# Create your models here.
