from django.shortcuts import render
from django.views import View
from booktest.models import BookInfo,HeroInfo
from django import http
from datetime import date
from django.db.models import F,Q
from django.db.models import Sum,Avg,Max,Min
# Create your views here.

class BooksView(View):
    # xxx/books/
    def get(self,request):

        # 构造上下文字典：将上下文字典中的数据渲染到模板中
        # context = {
        #     "name":"你爸爸",
        #     "age":111
        # }
        book = BookInfo.objects.all()
        context = {
            "book":book,
            "title":"沙比老师"
        }
        return render(request,"booktest/index.html",context)




class TestModelView2(View):
    # 查询测试：xxx/query1/

    def get(self,request):
        # 基本查询
        # 查询指定记录：只查询第一条记录，优先选get()，默认只查一条记录
        # book = BookInfo.objects.get(id=8)

        # 查询表中所有记录
        # all(),不能加条件
        # book = BookInfo.objects.all()
        # print(book)
        # return http.HttpResponse("查询成功")

        # 查询记录的个数：查询表中所有记录的个数
        # book = BookInfo.objects.all().count()

        # 查询满足条件的记录个数：查询未被逻辑删除的数据个数
        # book = BookInfo.objects.filter(is_delete=False).count()
        # print(book)
        # return http.HttpResponse("查询成功")

        # 过滤查询
        # 过滤查询的语法：模型类.objects.filter(属性__条件表达式=值)
        # 1.查询书名为天龙八部的个数
        # book = BookInfo.objects.filter(btitle__exact="三国演义").count()
        # 可简写
        # book = BookInfo.objects.filter(btitle="三国演义")

        # 2.查询书名包含“湖”的书籍（模糊查询）
        # book = BookInfo.objects.filter(btitle__contains="湖")

        # 3.查询书名以“部”为结尾的数集（模糊查询）
        # book = BookInfo.objects.filter(btitle__endswith="部")

        # 4.查询书名不为空的书籍（空查询）
        # book = BookInfo.objects.filter(btitle__isnull=False)

        # 5.查询编号为1或3或5的图书（范围查询）
        # book = BookInfo.objects.filter(id__in=[1,3,5])
        # 如果写id__in=[1,5],则表示查询1和5号

        # 6.查询编号大于3的书籍
        # book = BookInfo.objects.filter(id__gt=3)

        # 7.查询id不等于3的书籍（不相等）
        # exclude():跟filter一样的，也是一种过滤查询
        # exclude():查询指定的条件以外的数据
        # filter():查询满足指定条件的数据
        # book = BookInfo.objects.exclude(id=3)

        # 8.查询1990年1月1日后发表的书籍
        # book = BookInfo.objects.filter(bpub_date__gt="1990-1-1")
        # 或
        # book = BookInfo.objects.filter(bpub_date__gt=date(1990,1,1))  #要导包


        # F对象和Q对象
        # F对象
        # 1.查询阅读量大于评论量的书籍
        # book = BookInfo.objects.filter(bread__gt=F("bcomment"))

        # 2.查询阅读量大于2倍评论量的书籍
        # book = BookInfo.objects.filter(bread__gt=F("bcomment")*2)

        # Q对象
        # 1.查询阅读量大于20，或编号小于3的图书
        # book = BookInfo.objects.filter(Q(bread__gt=20),Q(id__lt=3))  #中间是逗号，代表且
        # book = BookInfo.objects.filter(Q(bread__gt=20)|Q(id__lt=3))    #中间是|，代表或

        # 2.查询阅读量大于10，并且发布时间在1980年1月1日之后
        # book = BookInfo.objects.filter(bread__gt=10,bpub_date__gt="1980-1-1")


        # 聚合函数
        # 1.统计总的阅读量
        # book = BookInfo.objects.aggregate(Sum("bread"))
        # print(book.get("bread__sum"))  #取出bread__sum这个值，不然会打印{'bread__sum': 366}

        # 2.统计阅读量的总平均数
        # book = BookInfo.objects.aggregate(Avg("bread"))


        # 正序：
        # book = BookInfo.objects.order_by("bread")
        # 倒序:
        # book = BookInfo.objects.order_by("-bread")


        # 一对多关联查询
        # 1.一查多:查询编号为1的图书中所有人物信息
        # 先查询出一方模型对象
        # hero = BookInfo.objects.get(id=1)
        # book = hero.heroinfo_set.all()

        # 2.多查一：查询编号为1的英雄出自的书籍
        # hero = HeroInfo.objects.get(id=1)
        # book = hero.hbook


        # 多对一条件查询
        # 1.查询图书，要求图书英雄为孙悟空
        # book = BookInfo.objects.filter(heroinfo__hname="孙悟空")

        # 2.查询图书，要求图书英雄的描述包含八
        # book = BookInfo.objects.filter(heroinfo__hcomment__contains="八")


        # 一对多条件查询
        # 1.查询书名为“天龙八部”的所有英雄
        # book = HeroInfo.objects.filter(hbook__btitle="天龙八部")

        # 2.查询图书阅读量大于30的所有英雄
        book = HeroInfo.objects.filter(hbook__bread__gt=30)
        print(book)
        return http.HttpResponse("查询成功")





# class TestModelView1(View):
#     # 测试增删改
#     # GET  xxx/data1/
#
#     def get(self,request):
#         # 新增：sava(),create()
#
#         # save()方法新增对象
#         # 使用模型类初始化模型对象
#         # book = BookInfo()
#         # # 给模型对象的属性赋值
#         # book.btitle = "西游记"
#         # book.bpub_date = "2000-01-02"
#         # book.bread = 20
#         # book.bcomment = 22
#         # # 逻辑删除项不赋值
#         # # book.is_delete = #无需赋值
#         # book.save()
#
#         # creat()方法
#         # 语法：模型类.模型类管理器.creat（模型属性=值）
#         # 模型管理器：是由Django提供并封装的一个对象（object），用语调用ORM的接口方法，固定的语法
#         # BookInfo.objects.create(
#         #     btitle = "三国演义",
#         #     bpub_date = "2001-12-12",
#         #     bread = 100,
#         #     bcomment = 222,
#         # )
#
#         # 修改：save(),update()
#         # save()
#             # 查询出要修改的记录/模型对象
#         # book = BookInfo.objects.get(id=5)
#         # book.btitle = "西游你改不改记"
#         # book.save()
#             # 新值覆盖旧值
#             # 同步新值
#
#         # update()
#         # 语法：模型类.objects.filter('条件').update(模型属性=新值)
#         # BookInfo.objects.filter(id=6).update(btitle="哈利波特")
#
#
#         # 物理删除：delete()
#         BookInfo.objects.filter(id=7).delete()
#         # 逻辑删除：模型对象 = 模型类.objects.get()  -->  模型对象.is_delete = True  -->  模型对象.save()
#         book = BookInfo.objects.get(id=8)
#         book.is_delete = True
#         book.save()
#         return http.HttpResponse("CHENGGONG")

