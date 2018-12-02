from django.db import models


class CourseType(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Course type"
        verbose_name_plural = "Courses type"


class Group(models.Model):
    signature = models.CharField(
        verbose_name="Signature",
        max_length=30
    )
    course_type = models.ForeignKey(
        CourseType,
        verbose_name='Course type',
        on_delete=models.SET_NULL,
        null=True
    )
    start_date = models.DateField(
        verbose_name="Start date",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.signature

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'


class Student(models.Model):
    name = models.CharField(
        max_length=33,
        verbose_name='Name'
    )
    surname = models.CharField(
        verbose_name='Surname',
        max_length=60
    )
    email = models.EmailField(
        verbose_name='E-mail'
    )
    github_nick = models.CharField(
        verbose_name='Github nick',
        max_length=100
    )
    group = models.ForeignKey(
        Group,
        verbose_name='Group',
        on_delete=models.CASCADE
    )
    exercises = models.ManyToManyField(
        'exams.Exercise',
        verbose_name='Exercise',
        through='exams.ExerciseStudent'
    )

    def __str__(self):
        return f'{self.name} {self.surname}("{self.github_nick}")'

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

