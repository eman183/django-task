# Generated by Django 4.1.4 on 2023-05-31 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0003_alter_login_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Std',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
