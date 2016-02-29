# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [

        migrations.AddField(
            model_name='coursescore',
            name='make_up',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='coursescore',
            unique_together=set([('student_id', 'course_id')]),
        ),

    ]
