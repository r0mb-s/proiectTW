# Generated by Django 5.1.3 on 2024-11-16 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_student_class_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='dashboard.quizclass'),
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number_of_questions', models.IntegerField()),
                ('questions', models.JSONField()),
                ('answers', models.JSONField()),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizes', to='dashboard.quizclass')),
            ],
        ),
    ]
