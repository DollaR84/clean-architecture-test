# Generated by Django 5.1.1 on 2024-09-12 23:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0006_alter_fileupload_options_alter_service_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fileupload',
            old_name='file',
            new_name='filename',
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('uuid_id', models.CharField(max_length=36, unique=True)),
                ('urls', models.TextField(null=True)),
                ('status', models.CharField(choices=[('not_started', 'Not Started'), ('pending', 'Pending'), ('parsing', 'Parsing'), ('saving', 'Saving'), ('done', 'Done'), ('error', 'Error')], default='not_started', max_length=12, verbose_name='Status')),
                ('file', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='parser.fileupload', verbose_name='Upload file')),
            ],
            options={
                'verbose_name': 'Uploaded data',
                'verbose_name_plural': 'Uploaded data',
                'db_table': 'uploads',
            },
        ),
    ]
