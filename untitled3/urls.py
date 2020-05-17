"""untitled3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include#将子路由包含进总路由

# 注册自定义路由转换器
# 1、导入注册路由转换器的方法
# 2、调用注册路由转换器的方法，完成路由转换器的注册
from django.urls.converters import register_converter
from converters import MobileConverter
# 注册函数
# register_converter("自定义的路由转换器","别名")
register_converter(MobileConverter,"mobile")



# 工程总路由
urlpatterns = [
    # 默认的后台管理系统的总路由，可以忽略
    path('admin/', admin.site.urls),
    # 将子应用中的子路由注册到总路由
    path("",include("ty6yt6.urls")),

    path("", include("response_request.urls"))


]
