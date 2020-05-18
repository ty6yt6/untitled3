from django.shortcuts import render,redirect,reverse
from django import http
from django.views import View
# Create your views here.
import json

# 以下代码演示响应

class LoginRedirectView(View):
    # 登录页面：POST http:xxxx/login_redirect/
    def post(self,request):
        # 如果用户登录成功后，把用户引导到首页（重定向）
        # return redirect("目标地址(注意要加根路径)")
        # 因为请求的发起者对应的地址是/login_redirect/
        # 要重定向到index/时，没有根路径时，结果就会把这个地址拼接到原链接，即/login_redirect/index/，所以会报错
        # 因此要加根路径。这时它就不会像上面那么处理。
        # 再或者，可以把完整链接写到地址处
        # return redirect("/index/")

        # 路由反向解析：解决重定向时达到动态地址效果
        # redirect(reserve('总路由别名:子路由的别名'))
        # ret_url = reverse("总路由别名：子路由别名")
        ret_url = reverse("zongluyou:index")
        return redirect(ret_url)

class IndexView(View):
    # 首页视图：GET http:127.0.0.1/index
    def get(self,request):
        return http.HttpResponse("这是一个首页")


class JSONResponseView(View):
    # GET xxxx/resp_json/
    def get(self,request):
        # json默认传的是字典数据，所以要准备一个字典，json会将该字典数据解析成json字符串，并且响应给客户端
        dict_data = {
            "name":"liubai",
            "age":11
        }
        return http.JsonResponse(dict_data)
        # 扩展：JsonResponse除了默认接受字典以外，是否可以接受其他的类型."safe"为True时，默认为字典，如果是False，则可以传列表数据或其他
        # return http.JsonResponse("列表数据",safe=False)

class Response1View(View):
    # 演示HttpResponse
    # GET xxxx/response1/
    # 提示：HttpResponse默认返回字符串
    # 如果想响应字符串以外数据，如图片：HttpResponse(响应体：图片的原始数据，content_type="image/jpg")
    def get(self,request):
        # return http.HttpResponse(content="响应体",content_type="数据类型(默认text/html)",status="状态码(默认200)",)
        # return http.HttpResponse(content="HttpResponse",content_type="text/html",status="200")
        return http.HttpResponse(content="HttpResponse")#(简写，因为后面两个有默认值，不写就等于默认)




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