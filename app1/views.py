#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#@File    :   views.py
#@Time    :   2019/12/26 10:47:25
# here put the import lib

from django.shortcuts import render, redirect, HttpResponse, reverse

from app1.models import Bock

import datetime
# Create your views here.


def book_add(request):
    """添加数据库控制器"""
    # bock = Bock(title='python',price=200,pub_date='2020-1-1')
    # bock.save()
    # print(bock.id)
    # print(request.method)
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        Bock.objects.create(title=title, price=price, pub_date=pub_date)
        return redirect('books')
    return render(request, 'book_add.html')


def books(request):
    '''查询'''
    bock = Bock.objects.all()
    return render(request, 'books.html', {'bock': bock})


def book_del(request, num):
    '''删除'''
    Bock.objects.filter(id=num).delete()
    return redirect('books')


def book_update(request, num):
    '''更新数据'''
    if request.method == 'POST':
        data = request.POST.dict()
        del data['csrfmiddlewaretoken']
        Bock.objects.filter(id=num).update(**data)
        return redirect('books')
    bock = Bock.objects.filter(id=num)
    return render(request, 'book_update.html', {'bock': bock})


def query(request):
    '''单表查询的方法'''
    # ret = Bock.objects.all() # all() 查询数据库所有的数据
    # ret = Bock.objects.filter(title='JAVA') # filter() 查询匹配的结果，不存在返回[]
    # ret = Bock.objects.all().exclude(title='GO') # exclude() 查询不符合条件的数据
    # ret = Bock.objects.get(title='GO') # get() 查询匹配的结果，返回结果是model对象并且结果只能是一个，除此之外报错
    # ret = Bock.objects.all().first() # first() 获取返回结果中的第一条，可链式操作，结果是model对象
    # ret = Bock.objects.all().last() # last() 获取返回结果中的最后一条，可链式操作，结果是model对象
    # ret = Bock.objects.all().order_by('title', '-price') 升降序
    # ret = Bock.objects.all().count() # count() 对查询出来的数据量计数，返回int类型
    # ret = Bock.objects.all().order_by('id').reverse() # reverse()  对查询结果反向排序
    # ret = Bock.objects.all().filter(title='111').exists()  # exists() 链式操作 对查询结果进行判断 有数据返回True 无则 false
    # ret = Bock.objects.all().values('title') # values() 查询所有匹配的数据，返回以关键字（字段）,相对应的数据。字典类型
    # ret = Bock.objects.all().values_list('title') # values_list 查询所有关键字对应的数据，元祖类型
    # ret = Bock.objects.all().values('title').distinct() # 查询所有匹配的数据，除去重复
    '''------模糊查询-------'''
    ret = Bock.objects.filter(
        pub_date__range=(datetime.datetime(2019, 11, 1, 0, 0),
                         datetime.datetime(2019, 11, 30, 0, 0))).values('title')
    print('-------', ret)
    return HttpResponse('ok')