# Generated by Django 5.0 on 2023-12-12 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_project_project_id_timesheet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.CharField(default='040a68e6c930', editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='projects',
            field=models.ManyToManyField(blank=True, to='core.project'),
        ),
    ]