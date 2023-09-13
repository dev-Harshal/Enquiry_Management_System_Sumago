# Generated by Django 4.2.5 on 2023-09-09 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry_department', '0002_rename_cource_course_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='Course_name',
            new_name='course_name',
        ),
        migrations.AlterField(
            model_name='followup',
            name='follow_up_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2023, 9, 9, 17, 57, 24, 531860)),
        ),
        migrations.AlterField(
            model_name='paymentdiscusion',
            name='first_installment_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 10, 17, 57, 24, 532858)),
        ),
    ]