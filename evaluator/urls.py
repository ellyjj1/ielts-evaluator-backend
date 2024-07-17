from django.urls import path
from .views import chatgpt_view

urlpatterns = [
    # 其他路由
    path('chatgpt/', chatgpt_view, name='chatgpt'),
]
