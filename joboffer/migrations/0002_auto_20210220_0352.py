# Generated by Django 3.1.6 on 2021-02-20 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joboffer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='city',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='company_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='job_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='salary',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='state',
            field=models.CharField(max_length=35),
        ),
    ]
