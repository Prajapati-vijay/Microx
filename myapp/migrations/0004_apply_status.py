# Generated by Django 4.1.3 on 2022-11-25 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_employer_id_apply_employer_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='status',
            field=models.CharField(default=None, max_length=15),
        ),
    ]