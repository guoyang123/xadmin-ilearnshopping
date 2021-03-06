# Generated by Django 2.0 on 2018-12-10 21:06

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('goods', '0002_auto_20181127_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='category_id',
        ),
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cates', to='category.Category', verbose_name='商品类别'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='detail',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', null=True, verbose_name='商品详情'),
        ),
    ]
