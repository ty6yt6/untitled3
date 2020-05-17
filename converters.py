# 自定义路由转换器
# 实现方式：复制源代码，把里面的正则改成自己想要的

class MobileConverter:

    regex = '1[3-9]\d{9}'

    def to_python(self,value):
        return int(value)

    def to_url(self,value):
        return str(value)