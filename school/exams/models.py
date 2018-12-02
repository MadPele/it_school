from django.db import models
from teams.models import CourseType, Student

class Exam(models.Model):
    course_type = models.ForeignKey(
        CourseType,
        verbose_name='Course type',
        on_delete=models.SET_NULL,
        null=True
    )
    name = models.CharField(
        verbose_name='Name',
        max_length=100
    )
    module_num = models.PositiveSmallIntegerField(
        verbose_name="Number of module"
    )

    def __str__(self):
        return f'{self.name}, Mod: {self.module_num}'

    class Meta:
        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'


class Exercise(models.Model):
    num = models.PositiveSmallIntegerField(
        verbose_name='Number of exercise'
    )
    points = models.PositiveSmallIntegerField(
        verbose_name='Points'
    )
    description = models.TextField(
        verbose_name='Content of exercise'
    )
    exam = models.ForeignKey(
        Exam,
        verbose_name='Exam',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return f'{self.exam}: {self.num}, max points={self.points}'

    class Meta:
        verbose_name = 'Exercise'
        verbose_name_plural = 'Exercises'


class ExerciseStudent(models.Model):
    student = models.ForeignKey(
        'teams.Student',
        verbose_name='Student',
        on_delete=models.CASCADE
    )
    exercise = models.ForeignKey(
        Exercise,
        verbose_name='Exercise',
        on_delete=models.CASCADE
    )
    points = models.PositiveSmallIntegerField(
        verbose_name='Points earned'
    )

    def __str__(self):
        return f'{self.student}:{self.exercise}(Earned: {self.points})'

    class Meta:

        verbose_name = 'Student exercise'
        verbose_name_plural = 'Student exercises'
