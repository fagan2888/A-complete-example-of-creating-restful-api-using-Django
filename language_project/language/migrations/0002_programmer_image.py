# Generated by Django 2.2.5 on 2019-09-10 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='programmer',
            name='image',
            field=models.ImageField(default='mark.jpg', upload_to='photos/%Y/%m/%d/'),
        ),
    ]