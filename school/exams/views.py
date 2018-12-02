from django.shortcuts import render
from teams.models import CourseType, Student
from django.views import View
from .models import Exam, Exercise, ExerciseStudent
from django.urls import reverse
from django.shortcuts import redirect


class CreateExam(View):
    template_name = 'exam.html'

    def get(self, request):
        exams = Exam.objects.all()
        courses = CourseType.objects.all()
        return render(request, self.template_name, {'exams': exams, 'courses': courses})

    def post(self, request):
        name = request.POST.get('name')
        number = request.POST.get('number')
        type_course_id = request.POST.get('type')
        course = CourseType.objects.get(pk=type_course_id)

        Exam.objects.create(name=name, module_num=number, course_type=course)
        return redirect(reverse('list-exams'))


def del_exam(request, exam_id):
    exam = Exam.objects.get(pk=exam_id)
    exam.delete()
    return redirect(reverse('list-exams'))


class CreateExercise(View):
    template_name = 'exercises.html'

    def get(self, request):
        exams = Exam.objects.all()
        exercises = Exercise.objects.order_by('exam')
        return render(request, self.template_name, {'exams': exams, 'exercises': exercises})

    def post(self,request):
        num = request.POST.get('num')
        points = request.POST.get('points')
        description = request.POST.get('description')
        exam_id = request.POST.get('exam')
        exam = Exam.objects.get(pk=exam_id)

        Exercise.objects.create(num=num, points=points, description=description, exam=exam)

        return redirect(reverse('add-exercises'))


class Select_exercises(View):
    template_name = 'select_exercises.html'

    def get(self, request):
        exams = Exam.objects.all()
        return render(request, self.template_name, {'exams': exams})

    def post(self, request):
        request.session['exam_id'] = request.POST.get('exam_id')
        return redirect(reverse('show-exercises'))



def show_exercises(request):
    exam_id = request.session.get('exam_id')
    exercises = Exercise.objects.filter(exam__pk=exam_id)
    name = Exam.objects.get(pk=exam_id)
    return render(request, 'show_exercises.html', {'exercises': exercises, 'name': name})


def select_data(request):
    if request.method == "GET":
        exams = Exam.objects.all()
        students = Student.objects.all()
        return render(request, 'data_for_exercises.html', {'exams': exams, 'students': students})
    else:
        choose = request.POST.get('choose')
        if choose == 'Show results':
            exam_id = request.POST.get('exam')
            student_id = request.POST.get('student')
            student = Student.objects.get(pk=student_id)
            exercises = Exercise.objects.filter(exam__pk=exam_id)
            exe_stu = ExerciseStudent.objects.filter(student__pk=student_id, exercise__in=exercises)
            exam = Exam.objects.get(pk=exam_id)
            return render(request, 'show_student_results.html', {'exercises': exercises, 'exe_stu': exe_stu,
                                                                 'student': student,'exam': exam})
        elif choose == 'Edit results':
            request.session['student'] = request.POST.get('student')
            request.session['exam'] = request.POST.get('exam')
            return redirect(reverse('save_exercises'))


def save_exercises(request):

    try:
        exercise_id = request.POST.get('exercise')
        exercise = Exercise.objects.get(pk=exercise_id)
        points = request.POST.get('points')
        student_id = request.session.get('student')
        student = Student.objects.get(pk=student_id)
        exam_id = request.session.get('exam')
        ExerciseStudent.objects.create(student=student, exercise=exercise, points=points)

    except:
        exam_id = request.session.get('exam')
        request.session['exam'] = exam_id
        student_id = request.session.get('student')
        request.session['student'] = student_id
        student = Student.objects.get(pk=student_id)

    exercises = Exercise.objects.filter(exam__pk=exam_id)
    exe_stu = ExerciseStudent.objects.filter(student__pk=student_id, exercise__in=exercises)
    exam = Exam.objects.get(pk=exam_id)
    return render(request, 'save_exercises.html', {'exercises': exercises, 'exe_stu': exe_stu, 'student': student,
                                                   'exam': exam})



def delete_stu_exe(request, exercise_id):
    exercise = ExerciseStudent.objects.get(pk=exercise_id)
    exercise.delete()
    return redirect(reverse('save_exercises'))


def delete_exercise(request, exercise_id):
    exercise = Exercise.objects.get(pk=exercise_id)
    exercise.delete()
    return redirect(reverse('show-exercises'))