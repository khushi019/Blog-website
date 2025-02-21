# Generated by Django 5.0.6 on 2024-07-13 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_alter_profile_image_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('-created_on',)},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='blog',
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
