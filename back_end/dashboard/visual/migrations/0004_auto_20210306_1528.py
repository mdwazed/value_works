# Generated by Django 3.1.7 on 2021-03-06 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visual', '0003_auto_20210306_1044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdevelopment',
            old_name='est_accuracy',
            new_name='test_accuracy',
        ),
    ]
