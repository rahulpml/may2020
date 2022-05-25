from django.urls import path
from . import views

urlpatterns = [
    path('',views.add_course,name='add_course'),
    path('add_student',views.add_student,name='add_student'),
    path('add_tutor',views.add_tutor,name='add_tutor'),
    path('sign_up',views.sign_up,name='sign_up'),
    path('log_in',views.log_in,name='log_in'),
    path('log_out',views.log_out,name='log_out'),
    path('home',views.home,name='home'),
    path('show_student',views.show_student,name='show_student'),
    path('show_course',views.show_course,name='show_course'),
    path('show_tutor',views.show_tutor,name='show_tutor'),
    path('student_details/<int:pk>',views.student_details,name='student_details'),
    path('edit_student/<int:pk>',views.edit_student,name='edit_student'),
    path('delete_student/<int:pk>',views.delete_student,name='delete_student'),
    path('edit_tutor/<int:pk>',views.edit_tutor,name='edit_tutor'),
    path('delete_tutor/<int:pk>',views.delete_tutor,name='delete_tutor'),
    path('edit_course/<int:pk>',views.edit_course,name='edit_course'),
    path('delete_course/<int:pk>',views.delete_course,name='delete_course'),
    
]