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
    re_path(r"^url_param3/(?P<phone_num>1[3-9]\d{9})/$",views.URLParam3View.as_view())
]