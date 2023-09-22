# Generated by Django 3.2.18 on 2023-09-14 05:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enquiry_department', '0003_rename_course_name_course_course_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='follow_up_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2023, 9, 14, 10, 59, 22, 227720)),
        ),
        migrations.AlterField(
            model_name='paymentdiscusion',
            name='first_installment_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 15, 10, 59, 22, 227721)),
        ),
        migrations.CreateModel(
            name='UserExtraInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('Enquiry', 'Enquiry'), ('Accounts', 'Accounts'), ('IT', 'IT')], max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
