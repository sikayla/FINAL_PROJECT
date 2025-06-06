# ==========================
# IMPORTS
# ==========================
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Subject, Grade
from .forms import StudentForm, SubjectForm, GradeForm 


# ==========================
# STUDENT VIEWS
# ==========================

# Display student list with count
def student_list(request):
    students = Student.objects.all()
    student_count = students.count()
    return render(request, 'index.html', {
        'students': students,
        'student_count': student_count
    })

# View student details
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'detail.html', {'student': student})

# About page
def about(request):
    return render(request, 'about.html')

# Add new learner
def add_learner(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_learner.html', {'form': form})

# Update student
def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('student_detail', pk=student.pk)
    return render(request, 'update_student.html', {'form': form})

# Delete student
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'delete_student.html', {'student': student})


# ==========================
# SUBJECT VIEWS
# ==========================

# Update subject
def update_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    form = SubjectForm(request.POST or None, instance=subject)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('student_detail', pk=subject.student.pk)
    return render(request, 'update_subject.html', {'form': form})

# Delete subject
def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    student_id = subject.student.id
    if request.method == 'POST':
        subject.delete()
        return redirect('student_detail', pk=student_id)
    return render(request, 'delete_subject.html', {'subject': subject})


# ==========================
# GRADE VIEWS
# ==========================

# Update grade
def update_grade(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    form = GradeForm(request.POST or None, instance=grade)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('student_detail', pk=grade.subject.student.pk)
    return render(request, 'update_grade.html', {'form': form})

# Delete grade
def delete_grade(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    student_id = grade.subject.student.id
    if request.method == 'POST':
        grade.delete()
        return redirect('student_detail', pk=student_id)
    return render(request, 'delete_grade.html', {'grade': grade})

# Add new grade
def add_grade(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.subject = subject
            grade.save()
            return redirect('student_detail', pk=subject.student.id)
    else:
        form = GradeForm()
    return render(request, 'add_grade.html', {'form': form, 'subject': subject})
