"""
1、创建自定义频率类并继承`SimpleRateThrottle`

2、在类中设置一个`scope`类属性，属性名随意

3、在settings中设置scope访问频次，格式为`{”scope属性名“:"访问频次"}`

4、在自定义的类中提供`get_cache_key`方法
"""
from rest_framework.throttling import SimpleRateThrottle


class MyThrottle(SimpleRateThrottle):
    scope = "mmm"

    def get_cache_key(self, request, view):
        phone = request.query_params.get("phone")

        # 没有手机号 不能限制
        if not phone:
            return None

        # 返回数据 根据手机号动态展示返回的值
        return "throttle_%(scope)s_%(ident)s" % {"scope": self.scope, "ident": phone}

