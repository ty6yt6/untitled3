from django.urls import path
from . import views
# urlpatterns = [
#     #使用路由匹配请求地址，每匹配成功一个就执行对应的函数视图逻辑
#     # path("网络地址正则表达式",视图函数名)
#     # 用户注册函数视图：http://127.0.0.1:8000/users/register/
#     path("1/register", views.register),
#     path("1/tupi",views.tupi),
# ]

# 用户注册类视图：http://127.0.0.1:8000/users/register/
urlpatterns = [
    # path("网络地址正则表达式",类视图名.as_view())
    # 注意：在给类视图注册子路由时，需要将类视图转为函数视图    类视图名.as_view()
    path("ty6yt6/register",views.RegisterView.as_view())
]