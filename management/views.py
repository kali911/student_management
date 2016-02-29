# -*- coding: utf-8 -*-
from django.db import connection
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render_to_response

import json

def json_response(response_dict, status=200):
    response = HttpResponse(json.dumps(response_dict), content_type="application/json", status=status)
    #response['Access-Control-Allow-Origin'] = '*'
    #response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
# Create your views here.
def search_st_id(request):
    if request.method == 'POST':
        cursor = connection.cursor()
        student_id = request.POST.get('student_id')

        sql = '''SELECT * FROM Student 
        WHERE student_id = \'%s\' 
        ''' % student_id

        try:
            cursor.execute(sql)
            data = dictfetchall(cursor)
            print data
            return render_to_response('st_result.html', locals())
        except IntegrityError:
            result = 0
        
    return render_to_response('st_search.html', locals())

def search_st_name(request):
    if request.method == 'POST':
        cursor = connection.cursor()
        student_name = request.POST.get('student_name')

        sql = '''SELECT * FROM Student 
               WHERE student_name = \'%s\' 
            ''' % student_name
        
        try:
            cursor.execute(sql)
            data = dictfetchall(cursor)
            return render_to_response('st_result.html', locals())
        except IntegrityError:
            result = 0
        
    return render_to_response('st_search.html', locals())

def search_st_major(request):
    if request.method == 'POST':
        cursor = connection.cursor()
        major_name = request.POST.get('major')

        sql = '''SELECT student_id, student_name, gender, birthday, 
                    Student.classroom_name, major_name 
                FROM Student, Major, Classroom 
                WHERE Student.classroom_name = Classroom.classroom_name 
                    AND Classroom.major_id = Major.id
                    AND major_name = \'%s\' 
            ''' % major_name
        
        try:
            cursor.execute(sql)
            data = dictfetchall(cursor)
            return render_to_response('st_result.html', locals())
        except IntegrityError:
            result = 0

    return render_to_response('st_search.html', locals())

def st_create(request):
    if request.method == 'POST':
        cursor = connection.cursor()
        student_id = request.POST.get('student_id')
        student_name = request.POST.get('student_name')
        gender = request.POST.get('gender')
        birthday = request.POST.get('birthday')
        classroom_name = request.POST.get('classroom_name')

        sql = '''
        INSERT INTO Student 
                    VALUES  ( \'%s\', \'%s\', \'%s\', \'%s\', \'%s\');
        ''' % (student_id, student_name, gender, birthday, classroom_name)

        try:
            result = cursor.execute(sql)
        except IntegrityError:
            result = 0
    return render_to_response('st_create.html', locals())

def sc_add(request):
    if request.method == 'POST':
        cursor = connection.cursor()
        student_id = request.POST.get('student_id')
        course_id = request.POST.get('course_id')
        score = int(request.POST.get('score'))
        make_up = int(request.POST.get('make_up', '0'))
        if make_up == 1:
            if score > 60:
                score = 60
                sql = '''UPDATE CourseScore
                SET make_up = 1, score = %d
                WHERE student_id = \'%s\' AND course_id = \'%s\'
                ''' % (score, student_id, course_id)
            else:
                sql = ''
        else:
            sql = '''
            INSERT INTO CourseScore (student_id, course_id, score, make_up)
                        VALUES  ( \'%s\', \'%s\', %d, %d);
            ''' % (student_id, course_id, score, make_up)

        try:
            result = cursor.execute(sql)
        except IntegrityError:
            result = 0
    return render_to_response('sc_add.html', locals())

def sc_add_auto(request):
    cursor = connection.cursor()
    input_file = open('/home/z-kidy/workspace/djcode/student_management/management/test.txt' ,'r').read()
    data = input_file.split('\n')
    for i in data:
        item =  i.split('/')
        sql = '''
        INSERT INTO CourseScore (score, course_id, student_id, make_up)
                    VALUES  ( %d, \'%s\', \'%s\', %d);
        ''' % (int(item[0]), item[1], item[2], int(item[3]) )
        result = cursor.execute(sql)
    return HttpResponse('ok')




def sc_search(request):
    if request.method == 'POST':
        cursor = connection.cursor()
        student_id = request.POST.get('student_id')

        sql = '''SELECT Course.course_id, course_name, property, teach_time,
        credit, score 
        FROM Course, CourseScore
        WHERE CourseScore.student_id = \'%s\' 
        AND Course.course_id = CourseScore.course_id
        ''' % (student_id)

        try:
            result = cursor.execute(sql)
            data = dictfetchall(cursor)
            return render_to_response('sc_search_result.html', locals())
        except IntegrityError:
            result = 0
    return render_to_response('sc_search.html', locals())

def sc_average(request):
    if request.method == 'POST':
        cursor = connection.cursor()
        student_id = request.POST.get('student_id')

        sql = '''SELECT credit, score 
        FROM Course, CourseScore
        WHERE CourseScore.student_id = \'%s\' 
        AND Course.course_id = CourseScore.course_id
        ''' % (student_id)

        try:
            result = cursor.execute(sql)
            data = dictfetchall(cursor)
            
            sum = 0
            credit_sum = 0
            for item in data:
                sum += item['score'] * item['credit']
                credit_sum += item['credit']

            averge = sum / credit_sum
            print averge

            sql_b = '''SELECT credit, score 
            FROM Course, CourseScore
            WHERE CourseScore.student_id = \'%s\' 
            AND Course.course_id = CourseScore.course_id
            AND Course.property = \'%s\'
            ''' % (student_id, u'必修')

            
            result_b = cursor.execute(sql_b)
            data_b = dictfetchall(cursor)
            
            sum_b = 0
            credit_sum_b = 0
            for item in data_b:
                sum_b += item['score'] * item['credit']
                credit_sum_b += item['credit']

            averge_b = sum_b / credit_sum_b
            print averge_b
            return render_to_response('sc_score_result.html', locals())
        except IntegrityError:
            result = 0
    return render_to_response('sc_score.html', locals())

def my_teachers(request):
    if request.method == 'POST':
        cursor = connection.cursor()
        student_id = request.POST.get('student_id')

        sql = '''SELECT course_name, teacher 
        FROM Course, CourseScore
        WHERE CourseScore.student_id = \'%s\' 
        AND Course.course_id = CourseScore.course_id
        ''' % (student_id)

        try:
            result = cursor.execute(sql)
            data = dictfetchall(cursor)
            return render_to_response('my_teachers.html', locals())
        except IntegrityError:
            result = 0
    return render_to_response('my_teachers.html', locals())

def warn(request):
    
    cursor = connection.cursor()

    sql = '''SELECT student_id, SUM(credit) credit_sum
    FROM CourseScore, Course
    WHERE CourseScore.course_id = Course.course_id AND score < 60 
    AND Course.course_id IN(
            SELECT course_id
            FROM Course
            WHERE property = \'%s\'
        )
    GROUP BY student_id
    HAVING SUM(credit) IN(12, 13, 14) 
    ''' % (u'必修')

    try:
        result = cursor.execute(sql)
        data = dictfetchall(cursor)
        print data
        sql_x = '''SELECT student_id, SUM(credit) credit_sum
        FROM CourseScore, Course
        WHERE CourseScore.course_id = Course.course_id AND score < 60 
        AND Course.course_id IN(
                SELECT course_id
                FROM Course
                WHERE property = \'%s\'
            )
        GROUP BY student_id
        HAVING SUM(credit) IN(17, 18, 19) 
        ''' % (u'选修')

        result = cursor.execute(sql_x)
        data_x = dictfetchall(cursor)
        print data_x
        return render_to_response('warn.html', locals())
    except IntegrityError:
        result = 0
    return render_to_response('warn.html', locals())
