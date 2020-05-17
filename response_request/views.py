from django.shortcuts import render
from django import http
from django.views import View
# Create your views here.
import json

class URLParam3View(View):
    # 测试re_path()提取路径参数
    # GET xx/url_param3/1822222222
    def get(self,request,phone_num):
        # 提取手机号
        return http.HttpResponse("re_path()实现的提取手机号：%s"%phone_num)



class URLParam2View(View):
    def get(self,request,phone_num):
        print(phone_num)
        return http.HttpResponse("测试手机号提取：%s"%phone_num)


class URLParam1View(View):
    # 测试path()提取普通路径参数：http://127.0.0.1:8000/url_param1/18/
    # 提取路径参数是在路由系统里完成的

    def get(self,request,age):
        # 视图内部的关键字要和路由中的关键字一样，比如：age

        return http.HttpResponse("测试path()提取普通路径参数：%s" % age)



class JSONParamView(View):
    # http://127.0.0.1:8000/json/
    # JSON中传递username，password
    # 方式：request.body
    def post(self,request):
        # 先获取原始的非表单类型的请求体数据，无论是什么都是使用request.body
        origin_data = request.body

        # 解析原始JSON数据
        # loads:将原始json数据转换为python字典形式
        json_dict = json.loads(origin_data)
        username = json_dict.get("username")
        password = json_dict.get("password")
        print(username,password)
        return http.HttpResponse("测试提取JSON数据")
        # 在解析json时，前端传送的json数据不对，则会报错，代码500。前端应该传raw（原始）


# 测试表单类型的请求体数据
class FormDataParamView(View):
    # POST http://127.0.0.1:8000/formdata/
    # 请求体中传递username，password
    def post(self,request):

        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)
        return http.HttpResponse("测试提取表单类型的请求体数据")


class QSParamView(View):
# 测试提取查询字符串
# http://127.0.0.1:8000/querystring/?name=zxc&age=18  GET
# 查询字符串方法和请求方法没有关系，GET,POST,PUT等都是用request.GET
    def get(self,request):
        name = request.GET.get("name")
        age = request.GET.get("age")

        return http.HttpResponse("查询字符串参数：%s--%s"%(name,age))

    def post(self,request):
        name = request.GET.get("name")
        age = request.GET.get("age")

        return http.HttpResponse("查询字符串参数：%s--%s"%(name,age))