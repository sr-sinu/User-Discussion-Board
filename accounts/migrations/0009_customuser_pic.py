# Generated by Django 4.0.5 on 2022-06-14 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='pic',
            field=models.ImageField(null=True, upload_to='media/images/'),
        ),
    ]