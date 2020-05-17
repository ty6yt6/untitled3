from django.shortcuts import render
from django import http
from django.views import View
# Create your views here.
import json

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