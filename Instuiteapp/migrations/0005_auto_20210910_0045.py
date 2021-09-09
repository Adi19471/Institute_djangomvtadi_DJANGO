# Generated by Django 3.2.7 on 2021-09-09 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instuiteapp', '0004_auto_20210908_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.BigIntegerField()),
                ('enquiry_data', models.TextField()),
                ('doute', models.CharField(choices=[('ui', 'Python Narayan'), ('rest-api', 'Srinivas'), ('Englis', 'Ratnakumar'), ('python', 'Narayana'), ('c', 'Jyothi'), ('django-doutes', 'DJANGO-ADI')], max_length=150)),
                ('date_of_post', models.DateTimeField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='coursedetailes',
            name='profiles',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
    ]
