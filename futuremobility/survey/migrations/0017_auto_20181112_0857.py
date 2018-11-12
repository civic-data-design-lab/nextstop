# Generated by Django 2.1.2 on 2018-11-12 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0016_auto_20181112_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='a',
            field=models.ManyToManyField(help_text='Survey response.', to='survey.Answer'),
        ),
        migrations.AlterField(
            model_name='response',
            name='age',
            field=models.CharField(choices=[(None, 'Not specified'), ('under-18', 'Under 18.'), ('18-24', '18-24'), ('25-34', '25-34'), ('35-44', '35-44'), ('45-54', '45-54'), ('55-64', '55-64'), ('65-plus', '65+.')], default='25-34', help_text='Age classes.', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='home',
            field=models.CharField(choices=[(None, 'Not specified'), ('urban', 'Urban'), ('suburban', 'Suburban'), ('rural', 'Rural')], default='urban', help_text='Type of location respondant calls home.', max_length=10, null=True),
        ),
    ]
