# Generated by Django 4.1 on 2022-09-04 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataApp', '0004_alter_student_form_alter_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(default='', max_length=25),
        ),
    ]
