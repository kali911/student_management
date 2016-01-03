from django.db import models

# Create your models here.
class Course(models.Model):
    'id primary_key'
    course_name = models.CharField(max_length=10)
    
    class Meta:
        db_table = 'Course'

class Major(models.Model):
    'id primary_key'
    major_name = models.CharField(max_length=10)

    class Meta:
        db_table = 'Major'

class Classroom(models.Model):
    # 'id primary_key'
    classroom_name = models.CharField(max_length=10, primary_key=True)
    major = models.ForeignKey(Major)

    class Meta:
        db_table = 'Classroom'

class Student(models.Model):
    student_id = models.CharField(max_length=15, primary_key=True)
    student_name = models.CharField(max_length=10)
    gender = models.CharField(max_length=2)
    birthday = models.CharField(max_length=10)
    classroom_name = models.ForeignKey(Classroom, db_column='classroom_name')

    class Meta:
        db_table = 'Student'

class TeachPlan(models.Model):
    course = models.ForeignKey(Course)
    classroom_name = models.ForeignKey(Classroom, db_column='classroom_name')
    property = models.CharField(max_length=10)
    teach_time = models.CharField(max_length=10)
    credit = models.FloatField()
    teacher = models.CharField(max_length=10)

    class Meta:
        db_table = 'TeachPlan'
        unique_together = ("teacher", "classroom_name")

class CourseScore(models.Model):
    student_id = models.ForeignKey(Student, db_column='student_id')
    course = models.ForeignKey(TeachPlan)
    score = models.IntegerField()
    
    class Meta:
        db_table = 'CourseScore'

        