# Generated by Django 2.1.3 on 2018-11-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_exercisestudent'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='exercises',
            field=models.ManyToManyField(through='exams.ExerciseStudent', to='exams.Exercise', verbose_name='Exercise'),
        ),
    ]