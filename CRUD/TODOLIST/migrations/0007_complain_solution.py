# Generated by Django 4.0.4 on 2022-07-04 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODOLIST', '0006_remove_complain_solution'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='solution',
            field=models.CharField(default='no solution yet!', max_length=1000),
        ),
    ]
