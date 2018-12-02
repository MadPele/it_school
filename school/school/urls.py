
from django.contrib import admin
from django.urls import path
from teams.views import CreateCourseType, delete_course_type, CreateGroup, delete_group, delete_student, \
    CreateStudent
from exams.views import CreateExam, del_exam, CreateExercise, Select_exercises, show_exercises, select_data, \
    save_exercises, delete_stu_exe, delete_exercise

urlpatterns = [
    path('admin/', admin.site.urls),
    path('types', CreateCourseType.as_view(), name='list-type'),
    path('types/delete/<int:type_id>', delete_course_type, name='delete-type'),
    path('groups', CreateGroup.as_view(), name='list-group'),
    path('groups/delete/<int:group_id>', delete_group, name='delete-group'),
    path('students', CreateStudent.as_view(), name='list-students'),
    path('students/delete/<int:student_id>', delete_student, name='delete-student'),
    path('exams', CreateExam.as_view(), name='list-exams'),
    path('exams/delete/<int:exam_id>', del_exam, name='delete-exam'),
    path('exercises', CreateExercise.as_view(), name='add-exercises'),
    path('select_exercises', Select_exercises.as_view(), name='select-exercises'),
    path('show_exercises', show_exercises, name='show-exercises'),
    path('data_for_exercises', select_data, name='data_for_exercises'),
    path('save_exercises', save_exercises, name='save_exercises'),
    path('delete_stu_exe/<int:exercise_id>', delete_stu_exe, name='delete_stu_exe'),
    path('delete_exercise/<int:exercise_id>', delete_exercise, name='delete_exercise'),
]
