from . import views
from django.urls import path


app_name = 'boards'
urlpatterns = [
    path('create/', views.create_board, name='create_board'),
    path('<int:board_id>/', views.read_board_detail, name='detail'),
    path('list/', views.read_board_list, name='list'),
    path('comment/<int:board_id>/', views.read_board_comment, name='comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment),
    path('<int:board_id>/views/', views.update_views, name='update_views'),
]
