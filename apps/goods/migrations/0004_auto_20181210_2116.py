# Generated by Django 2.0 on 2018-12-10 21:16

from django.db import migrations
import simditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20181210_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='detail',
            field=simditor.fields.RichTextField(blank=True, null=True, verbose_name='详情内容'),
        ),
    ]
