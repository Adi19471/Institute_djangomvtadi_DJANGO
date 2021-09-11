# Generated by Django 3.2.7 on 2021-09-11 04:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Instuiteapp', '0020_auto_20210911_0937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emaildata',
            old_name='sub',
            new_name='subject',
        ),
        migrations.RemoveField(
            model_name='emaildata',
            name='msg',
        ),
        migrations.RemoveField(
            model_name='emaildata',
            name='to',
        ),
        migrations.AddField(
            model_name='emaildata',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emaildata',
            name='message',
            field=models.TextField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='doute_course',
            field=models.CharField(choices=[('3', 'rest-api'), ('5', 'django-doutes'), ('4', 'c'), ('6', 'English'), ('1', 'python'), ('2', 'ui')], max_length=120),
        ),
        migrations.AlterField(
            model_name='contact',
            name='doute_triner',
            field=models.CharField(choices=[('python', 'Narayana'), ('ui', 'Python Narayan'), ('rest-api', 'Srinivas'), ('Englis', 'Ratnakumar'), ('django-doutes', 'DJANGO-ADI'), ('c', 'Jyothi')], max_length=150),
        ),
    ]