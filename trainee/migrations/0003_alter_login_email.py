# Generated by Django 4.1.4 on 2023-05-29 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0002_alter_login_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
