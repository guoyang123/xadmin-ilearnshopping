# Generated by Django 2.0 on 2018-11-27 23:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.IntegerField(default=0, verbose_name='父类id')),
                ('name', models.CharField(default='', help_text='类别名称', max_length=50, verbose_name='类别名称')),
                ('status', models.IntegerField(default=1, verbose_name='类别状态')),
                ('sort_order', models.IntegerField(default=0, verbose_name='排序')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '品类列表',
                'verbose_name_plural': '品类列表',
                'db_table': 'neuedu_category',
            },
        ),
    ]
