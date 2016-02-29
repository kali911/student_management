from django.db import models

class Major(models.Model):
    'id primary_key'
    major_name = models.CharField(max_length=10)

    class Meta:
        db_table = 'Major'

    def __unicode__(self):
        return self.major_name

class Classroom(models.Model):
    # 'id primary_key'
    classroom_name = models.CharField(max_length=10, primary_key=True)
    major = models.ForeignKey(Major)

    class Meta:
        db_table = 'Classroom'

    def __unicode__(self):
        return self.classroom_name

class Student(models.Model):
    student_id = models.CharField(max_length=15, primary_key=True)
    student_name = models.CharField(max_length=10)
    gender = models.CharField(max_length=2)
    birthday = models.CharField(max_length=10)
    classroom_name = models.ForeignKey(Classroom, db_column='classroom_name')

    class Meta:
        db_table = 'Student'

    def __unicode__(self):
        return self.student_name

class Course(models.Model):
    course_id = models.CharField(max_length=10, primary_key=True)
    course_name = models.CharField(max_length=10)
    classroom_name = models.ForeignKey(Classroom, db_column='classroom_name')
    property = models.CharField(max_length=10)
    teach_time = models.CharField(max_length=10)
    credit = models.FloatField()
    teacher = models.CharField(max_length=10)

    class Meta:
        db_table = 'Course'
        unique_together = ("teacher", "classroom_name")
    
    def __unicode__(self):
        return self.course_id


class CourseScore(models.Model):
    student_id = models.ForeignKey(Student, db_column='student_id')
    course_id = models.ForeignKey(Course, db_column='course_id')
    score = models.IntegerField()
    make_up = models.IntegerField(default=0)

    class Meta:
        db_table = 'CourseScore'
        unique_together = ("student_id", "course_id")

    def __unicode__(self):
        return self.student_id + 'by ' + self.course_id