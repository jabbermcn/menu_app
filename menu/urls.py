from django.urls import path

from .views import IndexPageView, Index1PageView

app_name = 'menu'

urlpatterns = [
    path('menu/', IndexPageView.as_view(), name='index'),
    path('menu1/', Index1PageView.as_view(), name='index')
]
