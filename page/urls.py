from django.urls import path
from . import views

urlpatterns = [
    # path('map/', views.maps),
    path('', views.main), # url 에 아무것도 입력되지 않으면 view.py 의 main 을 보여준다.
]