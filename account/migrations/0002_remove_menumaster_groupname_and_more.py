# Generated by Django 4.0.3 on 2023-01-02 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menumaster',
            name='groupname',
        ),
        migrations.RemoveField(
            model_name='taskfieldmaster',
            name='fieldtaskfield',
        ),
        migrations.RemoveField(
            model_name='taskfieldmaster',
            name='tasktaskfield',
        ),
        migrations.RemoveField(
            model_name='taskfieldmaster',
            name='usertaskfield',
        ),
        migrations.RemoveField(
            model_name='taskmaster',
            name='lastupdateuser',
        ),
        migrations.RemoveField(
            model_name='taskmaster',
            name='task',
        ),
        migrations.RemoveField(
            model_name='usertaskaccess',
            name='taskacc',
        ),
        migrations.RemoveField(
            model_name='usertaskaccess',
            name='useracc',
        ),
        migrations.RemoveField(
            model_name='user',
            name='comp',
        ),
        migrations.RemoveField(
            model_name='user',
            name='usr',
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.DeleteModel(
            name='FieldMaster',
        ),
        migrations.DeleteModel(
            name='MenuGroup',
        ),
        migrations.DeleteModel(
            name='MenuMaster',
        ),
        migrations.DeleteModel(
            name='TaskFieldMaster',
        ),
        migrations.DeleteModel(
            name='TaskMaster',
        ),
        migrations.DeleteModel(
            name='UserTaskAccess',
        ),
    ]