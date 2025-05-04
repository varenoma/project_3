from django.urls import path

from student.views import add_student, delete_student, edit_student, student_detail, student_list

app_name = 'student'

urlpatterns = [
    path('', student_list, name='student_list'),
    path('<int:pk>', student_detail, name='student_detail'),
    path('add/', add_student, name='add_student'),
    path('<int:pk>/edit', edit_student, name="edit_student"),
    path('<int:pk>/delete', delete_student, name="delete_student"),
]