# Generated by Django 4.0.4 on 2022-07-14 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TODOLIST', '0010_alter_sclass_complain1_alter_sclass_solution'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complain',
            name='user',
        ),
        migrations.DeleteModel(
            name='Sclass',
        ),
    ]
