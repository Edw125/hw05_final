# Generated by Django 2.2.9 on 2021-12-24 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts/', verbose_name='Картинка'),
        ),
    ]