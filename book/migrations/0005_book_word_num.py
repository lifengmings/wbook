# Generated by Django 2.0.3 on 2018-06-15 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_chapter_word_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='word_num',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]