from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('register',views.register,name="register"),
    path('update/<int:ID>',views.update_trainee,name="update_trainee"),
    path('delete/<int:id>',views.delete_trainee,name="delete_trainee"),
    path('alltrainee',views.list_trainee,name="list_trainee"),
    path('logout',views.logout,name="logout"),
    path('login',views.login,name="login")

]

