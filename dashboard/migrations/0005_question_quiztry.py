# Generated by Django 4.2.16 on 2024-11-16 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_student_class_name_quiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('answer_1', models.CharField(max_length=255)),
                ('answer_2', models.CharField(max_length=255)),
                ('answer_3', models.CharField(max_length=255)),
                ('answer_4', models.CharField(max_length=255)),
                ('correct_answer', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='QuizTry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('answers', models.JSONField()),
                ('quiz_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to='dashboard.quiz')),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='dashboard.student')),
            ],
        ),
    ]
