from django.urls import path
from . import views

urlpatterns = [
    path('',views.course,name="course"),
    path('update_course/<int:id>',views.update_course,name="update_course"),
    path('delete_course/<int:ID>',views.delete_course,name="delete_course"),
    path('add_course',views.add_course,name="add_course"),


]