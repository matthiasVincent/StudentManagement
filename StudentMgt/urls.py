from django.urls import path
from . import views, AdminView, studentviews

urlpatterns = [
    path('', views.index, name='index'),
    path('admin_page/', AdminView.admin_page, name="admin_page"),
    path('admin_login/', AdminView.admin_login, name='admin_login'),
    #path('login/', views.login, name='login'),
    #path('stuhome/<admin_no>/', views.stuhome, name='stuhome'),
    #path('stuhome/<admin_no>/subjects/', views.subject, name='subject'),
    #path('stuhome/<admin_no>/course/', views.course, name='course'),
    #path('stuhome/<admin_no>/classMates/', views.classMates, name='classMates'),
    path('logout_admin/', AdminView.logout_admin, name='logout_admin'),
    path('adduser/', AdminView.add_user, name='add_user'),
    path('save_add/', AdminView.save_add, name='save_add'),
    path('stulogin/', studentviews.stulogin, name='stulogin'),
    path('stuhome/', studentviews.stuhome, name='stuhome'),
    path('logout_student',studentviews.logout_student,name='logout_student')
]