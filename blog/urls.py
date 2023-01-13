from django.urls import path
from . import views
urlpatterns = [
    # 나중에 채움
    path('<int:value>/',	views.single_post_page),
    path('',	views.index),
]
