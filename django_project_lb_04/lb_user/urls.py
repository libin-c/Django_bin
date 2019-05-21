from django.conf.urls import url, include
from django.contrib import admin

from lb_user import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # 模板路由
    url(r'^', views.Templates_demo.as_view()),
]