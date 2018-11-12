# Generated by Django 2.1.2 on 2018-11-12 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0013_auto_20181112_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='back',
            field=models.FilePathField(help_text='Path to card back scan.', match='.*-back\\.png$', null=True, path='/static/cards/fg1/q1/', recursive=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='front',
            field=models.FilePathField(help_text='Path to card front scan.', match='.*-front\\.png$', null=True, path='/static/cards/fg1/q1/', recursive=True),
        ),
    ]
