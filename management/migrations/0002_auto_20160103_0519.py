# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursescore',
            name='student',
            field=models.ForeignKey(to='management.Student', db_column=b'student_id'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=15, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
