from django.urls import path
from . import views  # blog/views.pyからインポート

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),  # ルート: 一覧
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # 詳細
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),  # 新規作成
]