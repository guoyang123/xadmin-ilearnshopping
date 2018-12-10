# Generated by Django 2.1.3 on 2018-11-26 14:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', help_text='用户名', max_length=50, verbose_name='用户名')),
                ('password', models.CharField(default='', help_text='密码', max_length=50, verbose_name='密码')),
                ('email', models.EmailField(max_length=50, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=11, verbose_name='移动电话')),
                ('question', models.CharField(default='', help_text='问题', max_length=100, verbose_name='问题')),
                ('answer', models.CharField(default='', help_text='答案', max_length=100, verbose_name='答案')),
                ('role', models.IntegerField(default=1, verbose_name='用户角色')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '会员管理',
                'verbose_name_plural': '会员管理',
                'db_table': 'neuedu_user',
            },
        ),
    ]