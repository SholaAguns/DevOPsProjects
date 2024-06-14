# Generated by Django 5.0.6 on 2024-06-14 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytutor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='response',
            options={'ordering': ['-created_dt']},
        ),
        migrations.RemoveField(
            model_name='response',
            name='published_date',
        ),
        migrations.AddField(
            model_name='query',
            name='request',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='response',
            name='created_dt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]