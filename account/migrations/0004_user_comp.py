# Generated by Django 4.0.3 on 2023-01-02 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_fieldmaster_menugroup_menumaster_usertaskaccess_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='comp',
            field=models.CharField(default=True, max_length=100),
        ),
    ]