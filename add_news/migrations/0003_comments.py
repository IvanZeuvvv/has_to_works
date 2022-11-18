# Generated by Django 2.2 on 2022-11-01 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('add_news', '0002_auto_20221027_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='Имя пользователя')),
                ('text_comment', models.TextField(verbose_name='Текст комментария')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('news', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_news', to='add_news.Articles', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
