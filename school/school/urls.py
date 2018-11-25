
from django.contrib import admin
from django.urls import path
from teams.views import CreateCourseType, delete_course_type, CreateGroup, delete_group, delete_student, \
    CreateStudent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('types/delete/<int:type_id>', delete_course_type, name='delete-type'),
    path('groups/delete/<int:group_id>', delete_group, name='delete-group'),
    path('types', CreateCourseType.as_view(), name='list-type'),
    path('groups', CreateGroup.as_view(), name='list-group'),
    path('students/delete/<int:student_id>', delete_student, name='delete-student'),
    path('students', CreateStudent.as_view(), name='list-students'),
]
