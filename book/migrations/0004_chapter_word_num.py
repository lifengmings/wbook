# Generated by Django 2.0.3 on 2018-06-13 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_remove_chapter_word_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='word_num',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]