# Generated by Django 4.1.4 on 2023-05-31 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0010_register_remove_login_email_remove_login_password_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
    ]