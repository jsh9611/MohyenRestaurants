from django.urls import path
from . import views

urlpatterns = [
    path('delete/<int:pk>', views.PostDelete, name = 'delete'), # 글 삭제. 
    path('search/<str:q>/', views.PostSearch.as_view()), # board/search/검색어 로 접근하면 PostSearch 에서 처리
    path('delete_comment/<int:pk>/', views.delete_comment), # 댓글 삭제를 위한 URL 추가
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()), # 댓글 수정 페이지의 경로 추가
    path('update_post/<int:pk>/', views.PostUpdate.as_view()), # update_post/pk/ 로 이동 시 views.py의 PostUpdate 이 처리한다.
    path('create_post/', views.PostCreate.as_view()), # board/create_post 로 url 입력 시 views.py 의 PostCreate 클래스 사용
    path('category/<str:slug>/', views.category_page), # category 별 이동 경로 추가
    path('<int:pk>/new_comment/', views.new_comment), # 코멘트 작성
    path('', views.PostList.as_view()), # /board/ 링크로 이동 시 views.py 의 PostList 가 처리.
    path('<int:pk>/', views.PostDetail.as_view()), # /board/pk/ 로 이동 시 views.py 의 PostDetail 이 처리.
]
