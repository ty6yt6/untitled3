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

#
class RegisterView(View):
    def get(self, request):
        return http.HttpResponse("返回注册页面")

    def post(self, request):
        return http.HttpResponse("实现注册逻辑")