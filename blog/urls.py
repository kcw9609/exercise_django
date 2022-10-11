from django.urls import path
from . import views


# 앞에pk를 viws--에 넘긴다는 의미
urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),

]
