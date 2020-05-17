from django.shortcuts import render
from django import http
from django.views import View
# def register(request):
#     return http.HttpResponse("你看我像不像注册")
# # Create your views here.
#
# def tupi(request):
#     return http.HttpResponse("wuliao")

# 定义类视图
# class 类名(View):
#   请求方法可以是POST/GET等等
#   def 跟请求方法同名的函数名(self,request):
#         return 响应对象

# 以下代码用户演示path()、re_path()
class LoginView(View):
    # 用户登录类视图:
    # 地址：http://127.0.0.1:8000/users/login/

    def get(self,request):
        return http.HttpResponse("这是个登录页面")




# 类视图添加扩展类体现复用性
# python中自定义扩展类，通常以·Mixin·结尾
class ListModelMixin(object):
    # 扩展一个输出的功能
    # list扩展类
    def list(self,request,*args,**kwargs):
        pass

class CreateModelMixin(object):
    def create(self,request,*args,**kwargs):
        pass

# 将上两个类（父类）继承到这个类（子类）中，可以直接调用父类中的功能
class RegisterView(View,ListModelMixin,CreateModelMixin):
    def get(self, request):
        self.list(request)
        return http.HttpResponse("返回注册页面")

    def post(self, request):
        self.create(request)
        return http.HttpResponse("实现注册逻辑")