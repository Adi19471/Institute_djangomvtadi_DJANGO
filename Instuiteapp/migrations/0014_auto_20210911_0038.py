# Generated by Django 3.2.7 on 2021-09-10 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instuiteapp', '0013_auto_20210911_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='doute_course',
            field=models.CharField(choices=[('6', 'English'), ('1', 'python'), ('2', 'ui'), ('3', 'rest-api'), ('4', 'c'), ('5', 'django-doutes')], max_length=120),
        ),
        migrations.AlterField(
            model_name='contact',
            name='doute_triner',
            field=models.CharField(choices=[('python', 'Narayana'), ('ui', 'Python Narayan'), ('Englis', 'Ratnakumar'), ('django-doutes', 'DJANGO-ADI'), ('c', 'Jyothi'), ('rest-api', 'Srinivas')], max_length=150),
        ),
    ]
