from django.urls import path
from api import views


app_name = 'api'
urlpatterns = [
    path('post/list/', views.ApiPostLV.as_view(), name='post_list'),
    path('post/<int:pk>/', views.ApiPostDV.as_view(), name='post_detail'),
    path('post/catetag/', views.ApiCateTagView.as_view(), name='cate_tag'),
    path('post/comment/add/', views.ApiAddComment.as_view(), name='add_comment'),
]
