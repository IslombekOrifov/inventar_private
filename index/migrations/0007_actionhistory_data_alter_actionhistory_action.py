# Generated by Django 4.0.6 on 2023-07-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_actionhistory_changed_model_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionhistory',
            name='data',
            field=models.JSONField(default='salom'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='actionhistory',
            name='action',
            field=models.CharField(max_length=10),
        ),
    ]
