# Generated by Django 2.0.3 on 2018-06-04 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='书名')),
                ('cover', models.ImageField(blank=True, upload_to='cover', verbose_name='封面')),
                ('summary', models.TextField(verbose_name='简介')),
                ('status', models.CharField(choices=[('连载', '连载'), ('完本', '完本')], default='连载', max_length=10, verbose_name='状态')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Author', verbose_name='作者')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('仙侠', '仙侠'), ('玄幻', '玄幻'), ('都市', '都市'), ('科幻', '科幻'), ('历史', '历史'), ('游戏', '游戏'), ('灵异', '灵异'), ('武侠', '武侠')], max_length=10, verbose_name='分类')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='章节')),
                ('contents', models.TextField(verbose_name='内容')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('book_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='卷名')),
                ('book_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='volume_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Volume'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Category', verbose_name='分类'),
        ),
    ]
