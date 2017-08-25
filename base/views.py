#encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .models import para_data,essay_data,article_data

# 首页
def index(request):
    size = 6
    rec_sum = para_data.objects.filter(reco='yes').count()
    print rec_sum
    if rec_sum <= size:
         rec_start = 0
    else:
         rec_start = rec_num - size
    rec_end = rec_sum
    datas = para_data.objects.filter(reco='yes')[rec_start:rec_end]
    datas = reverse(datas.count(),datas)
    new_para = get_news('All')
    new_para = reverse(new_para.count(),new_para)             # 获取最新文章信息
    max_para = get_max('All')                                 # 获取点击最高文章信息
    return render(request, 'index.html',{'datas':datas,'new_para':new_para,'max_para':max_para})

# 关于我
def about(request):
    return render(request,'about.html')

# 心情随笔
def essay(request):
    '''处理页码逻辑'''
    page = request.GET['page']
    size = 10
    essay_sum = essay_data.objects.all().count()
    essay_start =  essay_sum - int(page) * size
    essay_end =  essay_sum - (int(page) - 1) * size
    if essay_start < 0:
         essay_start = 0
    datas = essay_data.objects.all()[essay_start:essay_end]
    page_data = list()
    url = '/essay?page='
    pages = get_pages(essay_sum,size)                         # 获取碎言碎语总页数
    page_data = arr_page(url,page,pages)                      # 获取有关页码的数据
    print(pages)
    print(page_data)
    # 处理img链接问题（img存储none字节，就不设置图片）
    for data in datas:
         if data.img != "none":
             data.img = '<img src="' + data.img + '">'
         else:
             data.img = ''
    datas = reverse(datas.count(),datas)                      # 数据倒序
    return render(request,'saylist.html',{'datas':datas,'page_data':page_data})

# 倒转数据
def reverse(datas_sum,datas):
    resuit = list()
    for i in range(0,datas_sum):
         resuit.append(datas[datas_sum-i-1])
    return resuit

# 获取页面总数
def get_pages(essay_sum,size):
    remainder = essay_sum % size
    if remainder <= 0:
         pages = essay_sum / size
    if remainder > 0:
         pages = essay_sum / size + 1
    return pages

# 页码处理
def arr_page(url,page,pages):
    page_data = list()
    page_data.append('<a title="Total record"><b>' + str(pages) + '</b></a>')
    if int(page) == 1:
         page_data.append('<b>' + page + '</b>')
         for i in range(2,pages+1):
              if i <= 5:
                   page_data.append('<a href="'+url+str(i)+'">'+str(i)+'</a>')
         if int(page) != pages:
              page_data.append('<a href="'+url+ str(2) +'">&gt;</a>')
              page_data.append('<a href="'+url+ str(pages) +'">&gt;&gt;</a>')
    if int(page) > 1 and int(page) <= pages:
         page_data.append('<a href="'+url+ str(1) +'">&lt;&lt;</a>')
         page_data.append('<a href="'+url+ str(int(page)-1) +'">&lt;</a>')
         for i in range(0,2):
              num = int(page) - 2 + i
              if num >= 1:
                   page_data.append('<a href="'+url+str(num)+'">'+str(num)+'</a>')
         page_data.append('<b>' + page + '</b>')
         for i in range(int(page)+1,pages+1):
              if i <= int(page)+2:
                   page_data.append('<a href="'+url+str(i)+'">'+str(i)+'</a>')
         if int(page) != pages:
              page_data.append('<a href="'+url+ str(int(page)+1) +'">&gt;</a>')
              page_data.append('<a href="'+url+ str(pages) +'">&gt;&gt;</a>')
    return page_data

# 获取点击排行
def get_max(kind):
    piece = 5
    find_sum = para_data.objects.all().count()
    dt = list(article_data.objects.all())
    fdata = list(para_data.objects.all())
    # 创建两个列表用于存储数据
    data = list()
    find_data = list()
    # 筛选不同的类型的文章数据
    if kind != 'All':
         for i in range(0,find_sum):
              if fdata[i].doc_type == kind:
                   print fdata[i].doc_type
                   data.append(dt[i])
                   find_data.append(fdata[i])
    else:
         data = dt
         find_data = fdata
    find_sum = len(find_data)
    # 冒泡算法进行排序
    for i in range(0,find_sum):
         for j in range(i+1,find_sum):
              if int(data[i].viewed) < int(data[j].viewed):
                   data[i],data[j] = data[j],data[i]
                   find_data[i],find_data[j] = find_data[j],find_data[i]
    # 讲排名前五的数据筛选出来
    resuit = list()
    for i in range(0,piece):
         if i < find_sum:
              resuit.append(find_data[i])
    return resuit

# 获取最新文章
def get_news(kind):
    piece = 5                    # 设置获取篇数
    # 判断获取的文章类型
    if kind == 'All':
         find_sum = para_data.objects.all().count()
    else:
         find_sum = para_data.objects.filter(doc_type=kind).count()
    # 计算查询的范围
    if find_sum <= piece:
         find_start = 0
    else:
         find_start = find_sum - piece
    find_end = find_sum
    # 根据文章类型来获取数据
    if kind =='All':
         data = para_data.objects.all()[find_start:find_end]
    else:
         data = para_data.objects.filter(doc_type=kind)[find_start:find_end]
    return data


# Create your views here.
