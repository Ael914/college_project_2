# Generated by Django 4.2.6 on 2024-01-17 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='overview_en',
            field=models.TextField(null=True, verbose_name='overview'),
        ),
        migrations.AddField(
            model_name='course',
            name='overview_ru',
            field=models.TextField(null=True, verbose_name='overview'),
        ),
        migrations.AddField(
            model_name='course',
            name='overview_zh_hans',
            field=models.TextField(null=True, verbose_name='overview'),
        ),
        migrations.AddField(
            model_name='course',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='course',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='course',
            name='title_zh_hans',
            field=models.CharField(max_length=200, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='course',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='course',
            name='overview',
            field=models.TextField(verbose_name='overview'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='file',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='file',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='file',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='updated'),
        ),
        migrations.AlterField(
            model_name='image',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='image',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='updated'),
        ),
        migrations.AlterField(
            model_name='module',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='module',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='text',
            name='content',
            field=models.TextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='text',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='text',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='text',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='updated'),
        ),
        migrations.AlterField(
            model_name='video',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='video',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='updated'),
        ),
    ]
