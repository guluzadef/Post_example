from django.urls import path

from .views import home,about,contact,register,login_view,usersetting,logout_view,profile_view,deleteview,post_data,detail_user,author_view,dashboard,update_view

urlpatterns = [
    path('', home, name="home"),
    path('about/',about,name="about"),
    path('contact/',contact,name="contact"),
    path('register/',register,name="register-view"),
    path('login/', login_view, name="login-view"),
    path('logout/',logout_view,name="logout-view"),
    path('profile/',profile_view,name="profile-view"),
    path('post/', post_data, name="post"),
    path('detailuser/<int:id>/',detail_user,name="detail-view"),
    path('author/<int:pk>/',author_view,name="author"),
    path('dashboard/',dashboard,name="dashboard"),
    path('dashboard/<int:id>/update',update_view,name="update"),
    path('dashboard/<int:id>/delete',deleteview,name="delete"),
    path('settings/',usersetting,name="setting")
]
