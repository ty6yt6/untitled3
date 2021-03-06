from django.urls import path,re_path
from . import views

urlpatterns = [
    # 查询字符串不是路径，是路径中的参数，所以路由不用匹配查询字符串
    # http://127.0.0.1:8000/querystring/?name=zxc&age=18  GET

    path("querystring/",views.QSParamView.as_view()),

    # http://127.0.0.1:8000/formdata/
    path("formdata/",views.FormDataParamView.as_view()),
    path("json/",views.JSONParamView.as_view()),
    # path("url_param1/18/",views.URLParam1View.as_view()),
    # 提取18:path("url_param1/<路由转换器，提取路径参数：变量（接收提取的路径参数）>/",views.URLParam1View.as_view()),
    path("url_param1/<int:age>/",views.URLParam1View.as_view()),

    path("url_param2/<mobile:phone_num>/",views.URLParam2View.as_view()),
    # 匹配完后要用正则表达式的组把正则提取出来（）
    re_path(r"^url_param3/(?P<phone_num>1[3-9]\d{9})/$",views.URLParam3View.as_view()),

    # /response1/
    path("response1/",views.Response1View.as_view()),

    # /resp_json/
    path("resp_json/",views.JSONResponseView.as_view()),

    # 以下路由演示重定向
    # 首页/index/
    # path("index/",views.IndexView.as_view()),
    # 注册页面/login_redirect/
    path("login_redirect/",views.LoginRedirectView.as_view()),

    # 动态重定向页面：给子路由起别名，为了让重定向页面可以动态获取
    path("index/",views.IndexView.as_view(),name="index"),
]