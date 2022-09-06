# Generated by Django 4.1 on 2022-09-04 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataApp', '0002_remove_student_desc_student_county_student_form_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='form',
            field=models.CharField(choices=[('Form One(1)', 'Form One(1)'), ('Form Two(2)', 'Form Two(2)'), ('Form Three(3)', 'Form Three(3)'), ('Form Four(4)', 'Form Four(4)')], max_length=15),
        ),
        migrations.AlterField(
            model_name='student',
            name='kcpe_marks',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='kcpe_years',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(default=12345678, help_text='Enter atlist 6 digit number', max_length=25),
        ),
    ]