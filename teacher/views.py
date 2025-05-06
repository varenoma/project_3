from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .forms import FormTeacher
from .models import TeacherDb
# Create your views here.


def teacher_list(request):
    data = TeacherDb.objects.all()
    return render(request, 'teacher/teacher_list.html', {'data': data})


def teacher_detail(request, pk):
    teacher = get_object_or_404(TeacherDb, pk=pk)
    return render(request, 'teacher/teacher_detail.html', {'teacher': teacher})


@login_required
def add_teacher(request):
    if request.method == 'POST':
        form = FormTeacher(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher:teacher_list')
    else:
        form = FormTeacher()
    return render(request, 'teacher/teacher_add.html', {'form': form})


@login_required
def edit_teacher(request, pk):
    teacher = get_object_or_404(TeacherDb, pk=pk)
    if request.method == 'POST':
        form = FormTeacher(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher:teacher_list')
    else:
        form = FormTeacher(instance=teacher)
    return render(request, 'teacher/teacher_edit.html', {'form': form, 'teacher': teacher})


@login_required
def delete_teacher(request, pk):
    teacher = get_object_or_404(TeacherDb, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher:teacher_list')
    return render(request, 'teacher/teacher_delete.html', {'teacher': teacher})