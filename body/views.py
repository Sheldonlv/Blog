#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from base.models import para_data,article_data
from base import views as base
from django.contrib import messages

# 时光荏苒
def time(request):
    kind = request.GET['type']
    page = request.GET['page']
    size = 5
    new_para = base.get_news(kind)                            # 获取最新文章信息
    new_para = base.reverse(new_para.count(),new_para)        # 对信息进行顺序调整
    max_para = base.get_max(kind)                             # 获取点击最高文章信息
    # 根据请求文章的类型进行数据索引
    if kind == 'All':
         find_sum = para_data.objects.all().count()
    else:
         find_sum = para_data.objects.filter(doc_type=kind).count()
    find_start = find_sum - int(page) * size
    find_end = find_sum - (int(page) - 1) * size
    if find_start < 0:
         find_start = 0
    # 同上根据文章类型进行数据索引
    if kind == 'All':
         datas = para_data.objects.all()[find_start:find_end]
    else:
         datas = para_data.objects.filter(doc_type=kind)[find_start:find_end]
    page_data = list()
    url = '/time?type=' + kind + '&page='
    pages = base.get_pages(find_sum,size)                         # 获取该类文章总页数
    page_data = base.arr_page(url,page,pages)                     # 获取有关页码的数据
    datas = base.reverse(datas.count(),datas)                     # 数据倒序
    return render(request,'diarylist.html',{'new_para':new_para,'max_para':max_para,'datas':datas,'page_data':page_data})

# 阅读全文
def article(request):
    ID = request.GET['id']
    para_datas = para_data.objects.get(Num=ID)
    article_datas = article_data.objects.get(Num=ID)
    article_datas.viewed = add_viewed(article_datas.viewed)
    article_datas.save()
    kind = para_datas.doc_type
    new_para = base.get_news(kind)                                # 获取最新文章信息
    new_para = base.reverse(new_para.count(),new_para)            # 对信息进行顺序调整
    max_para = base.get_max(kind)                                 # 获取点击最高文章信息
    link = list()                                                 # 存储上下文索引的列表
    # 上一篇文章索引
    if (int(ID)-1) > 100:
         last = para_data.objects.get(Num=str(int(ID)-1)).title
         link.append(u'上一篇：<a href="/article?id='+str(int(ID)-1)+'">'+last+'</a>')
    else:
         link.append(u'上一篇：<a href="#">'+''+'</a>')
    # 下一篇文章索引
    count = para_data.objects.all().count() - 1
    num = int(para_data.objects.all()[count].Num)
    if int(ID) == num:
         link.append(u'下一篇：<a href="#">'+''+'</a>')
    else:
         next = para_data.objects.get(Num=str(int(ID)+1))
         link.append(u'下一篇：<a href="/article?id='+str(int(ID)+1)+'">'+next.title+'</a>')
    return render(request,'new.html',{'para':para_datas,'article':article_datas,'new_para':new_para,'max_para':max_para,'link':link})

# 编辑文章的版面
# 该版面仅为实现功能而设立，暂不做过多优化
def edit(request):
    if request.method == 'POST':
         # 获取最新文章的ID
         num = para_data.objects.all().count()
         ID = para_data.objects.all()[num-1].Num
         # 从表单中获取各个数据
         title = request.POST['title'].encode('utf-8')            # 标题
         img = request.POST['img'].encode('utf-8')                # logo
         writer = request.POST['writer'].encode('utf-8')          # 作者
         doc_type = request.POST['type'].encode('utf-8')          # 文章类型
         reco = request.POST['reco'].encode('utf-8')              # 是否推荐
         abstract = request.POST['abstract'].encode('utf-8')      # 摘要
         content = request.POST['content'].encode('utf-8')        # 内容
         ps = request.POST['ps'].encode('utf-8')                  # 密码
         ID = str(int(ID) + 1)                                    # 文章ID
         viewed = 0                                               # 阅读次数
         # 进行密码判定
         if ps == '753951':
              # 然后将这些数据保存到数据库中
              para = para_data(Num = ID,title = title,img = img,writer = writer,doc_type = doc_type,reco = reco,content = abstract)
              para.save()
              article = article_data(Num = ID,content = content,viewed = viewed)
              article.save()
              return HttpResponseRedirect('/')                    # 重定向回首页
         else:
              return HttpResponse(u"你的密码有误!")
    return render(request,'edit.html')

# 留言板
def gustbook(request):
    return render(request,'gustbook.html')

# 阅读次数+1
def add_viewed(num):
    num = str(int(num) + 1)
    return num

# Create your views here.
