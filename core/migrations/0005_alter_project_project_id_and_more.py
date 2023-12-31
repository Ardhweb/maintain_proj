# Generated by Django 5.0 on 2023-12-12 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_project_project_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.CharField(default='36ade2bca52f', editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='hours_worked',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
