# Generated by Django 3.2.4 on 2021-06-23 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_id', models.CharField(max_length=10)),
                ('subject_name', models.CharField(max_length=128)),
                ('teacher_id', models.CharField(max_length=10)),
                ('teacher_name', models.CharField(max_length=20)),
                ('start_time', models.TimeField()),
                ('finish_time', models.TimeField()),
                ('attend_time', models.IntegerField()),
                ('late_time', models.IntegerField()),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
