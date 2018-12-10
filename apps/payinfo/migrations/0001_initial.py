# Generated by Django 2.0 on 2018-11-27 23:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PayInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='用户id')),
                ('order_no', models.IntegerField(verbose_name='订单号')),
                ('pay_platform', models.IntegerField(choices=[(1, '支付宝'), (2, '微信')], help_text='支付平台', verbose_name='支付平台')),
                ('platform_number', models.CharField(default='', max_length=200, verbose_name='流水号')),
                ('platform_status', models.CharField(default='', max_length=20, verbose_name='支付状态')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '支付列表',
                'verbose_name_plural': '支付列表',
                'db_table': 'neuedu_payinfo',
            },
        ),
    ]