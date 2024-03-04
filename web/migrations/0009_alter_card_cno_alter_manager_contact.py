# Generated by Django 4.1.4 on 2022-12-25 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_manager_id_borrow_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='cno',
            field=models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='卡号'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='contact',
            field=models.CharField(max_length=20, verbose_name='联系方式'),
        ),
    ]