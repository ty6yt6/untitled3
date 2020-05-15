from django.urls import path
from . import views
urlpatterns = [
    #使用路由匹配请求地址，每匹配成功一个就执行对应的函数视图逻辑
    # path("网络地址正则表达式",视图函数)
    # 用户注册：http://127.0.0.1:8000/users/register/
    path("1/register", views.register),
    path("1/tupi",views.tupi),
]

