from django.urls import path

from teacher.views import add_teacher, delete_teacher, edit_teacher, teacher_detail, teacher_list

app_name = 'teacher'

urlpatterns = [
    path('', teacher_list, name='teacher_list'),
    path('<int:pk>', teacher_detail, name='teacher_detail'),
    path('add/', add_teacher, name='add_teacher'),
    path('<int:pk>/edit', edit_teacher, name="edit_teacher"),
    path('<int:pk>/delete', delete_teacher, name="delete_teacher"),
]
