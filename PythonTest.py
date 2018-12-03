import pytz
from datetime import datetime

# 如果在seting中设置了 USE_TZ = True ，拿到的时间就是aware time
timeAware = datetime.now()
timeAware.astimezone(pytz.timezone("UTC"))

# 获取的是navie time的话需要replace转化一下
timeNavie = datetime.now()
timeNavie.replace(tzinfo = pytz.timezone("Asia/Shanghai"))
timeNavie.astimezone(pytz.timezone("UTC"))


from django.utils.timezone import now, localtime

time = now() # 在Django中会根据USER_TZ字段来判断是否使用utz时间
# def now():
#     if settings.USE_TZ:
#         # timeit shows that datetime.now(tz=utc) is 24% slower
#         return datetime.utcnow().replace(tzinfo=utc)
#     else:
#         return datetime.now() # 如果为False，这里在Linux中会拿到一个navie时间，从而无法转换为其他时区了

localtime(time) # 在Django中会根据TIME_ZONE配置的时区来转化时间。如果配置的时区会作用于模板 过滤器 tz

