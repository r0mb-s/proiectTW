# Generated by Django 5.1.3 on 2025-01-15 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_quizclass_account_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='answers',
            field=models.JSONField(default='{}'),
        ),
    ]