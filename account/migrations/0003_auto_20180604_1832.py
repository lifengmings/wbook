# Generated by Django 2.0.3 on 2018-06-04 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
        ('account', '0002_bookshelf'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookshelf',
            name='collection_books',
            field=models.ManyToManyField(to='book.Book'),
        ),
        migrations.AlterField(
            model_name='bookshelf',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
