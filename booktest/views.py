from django.shortcuts import render
from django.views import View
from booktest.models import BookInfo
from django import http
# Create your views here.

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
        book = BookInfo.objects.filter(is_delete=False).count()
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

