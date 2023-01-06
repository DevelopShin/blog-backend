from django.urls import path
from post import views


app_name = 'post'
urlpatterns = [
    path('<int:pk>/', views.PostDV.as_view(), name='post_detail')
]
