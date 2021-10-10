from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('login/user/', views.loginUser),
    path('create/user/', views.createUser),
    path('data/user/all', views.showUser),
    path('data/user/pagination', views.showUserPagination),
    path('data/user/render', views.UserPaginationHTML),
    path('update/user', views.updateUser),
    path('delete/user', views.deleteUser),
]
