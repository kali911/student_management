# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('classroom_name', models.CharField(max_length=10, serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'Classroom',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Course',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField()),
            ],
            options={
                'db_table': 'CourseScore',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('major_name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Major',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('student_name', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=2)),
                ('birthday', models.CharField(max_length=10)),
                ('classroom_name', models.ForeignKey(to='management.Classroom', db_column=b'classroom_name')),
            ],
            options={
                'db_table': 'Student',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeachPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('property', models.CharField(max_length=10)),
                ('teach_time', models.CharField(max_length=10)),
                ('credit', models.FloatField()),
                ('teacher', models.CharField(max_length=10)),
                ('classroom_name', models.ForeignKey(to='management.Classroom', db_column=b'classroom_name')),
                ('course', models.ForeignKey(to='management.Course')),
            ],
            options={
                'db_table': 'TeachPlan',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='teachplan',
            unique_together=set([('teacher', 'classroom_name')]),
        ),
        migrations.AddField(
            model_name='coursescore',
            name='Course',
            field=models.ForeignKey(to='management.TeachPlan'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coursescore',
            name='student',
            field=models.ForeignKey(to='management.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='classroom',
            name='major',
            field=models.ForeignKey(to='management.Major'),
            preserve_default=True,
        ),
    ]
