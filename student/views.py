from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .forms import FormStudent
from .models import StudentDb
# Create your views here.


def student_list(request):
    data = StudentDb.objects.all()
    return render(request, 'student/student_list.html', {'data': data})


def student_detail(request, pk):
    student = get_object_or_404(StudentDb, pk=pk)
    return render(request, 'student/student_detail.html', {'student': student})


@login_required
def add_student(request):
    if request.method == 'POST':
        form = FormStudent(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student:student_list')
    else:
        form = FormStudent()
    return render(request, 'student/student_add.html', {'form': form})


@login_required
def edit_student(request, pk):
    student = get_object_or_404(StudentDb, pk=pk)
    if request.method == 'POST':
        form = FormStudent(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student:student_list')
    else:
        form = FormStudent(instance=student)
    return render(request, 'student/student_edit.html', {'form': form, 'student': student})


@login_required
def delete_student(request, pk):
    student = get_object_or_404(StudentDb, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student:student_list')
    return render(request, 'student/student_delete.html', {'student': student})
