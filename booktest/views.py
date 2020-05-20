from django.shortcuts import render
from django.views import View
from booktest.models import BookInfo
from django import http
# Create your views here.
class TestModelView1(View):
    # 测试增删改
    # GET  xxx/data1/

    def get(self,request):
        # 新增：sava(),create()

        # save()方法新增对象
        # 使用模型类初始化模型对象
        # book = BookInfo()
        # # 给模型对象的属性赋值
        # book.btitle = "西游记"
        # book.bpub_date = "2000-01-02"
        # book.bread = 20
        # book.bcomment = 22
        # # 逻辑删除项不赋值
        # # book.is_delete = #无需赋值
        # book.save()

        # creat()方法
        # 语法：模型类.模型类管理器.creat（模型属性=值）
        # 模型管理器：是由Django提供并封装的一个对象（object），用语调用ORM的接口方法，固定的语法
        # BookInfo.objects.create(
        #     btitle = "三国演义",
        #     bpub_date = "2001-12-12",
        #     bread = 100,
        #     bcomment = 222,
        # )

        # 新增：save(),create()
        # save()
            # 查询出要修改的记录/模型对象
        # book = BookInfo.objects.get(id=5)
        # book.btitle = "西游你改不改记"
        # book.save()
            # 新值覆盖旧值
            # 同步新值
        # create()
        # 语法：模型类.objects.filter('条件').update(模型属性=新值)
        BookInfo.objects.filter(id=6).update(btitle="哈利波特")
        return http.HttpResponse("CHENGGONG")

