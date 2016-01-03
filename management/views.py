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

