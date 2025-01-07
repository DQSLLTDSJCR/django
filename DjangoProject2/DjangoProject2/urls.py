# DjangoProject2/urls.py
from django.urls import path,include

urlpatterns = [
    path('hello/', include('hello.urls')),  # 如果你有 hello 视图  # 添加根路径处理
    path('', include('neko.urls')),
    path('',include('API.urls'))
]
