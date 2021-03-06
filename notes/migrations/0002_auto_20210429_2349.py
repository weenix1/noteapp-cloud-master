# Generated by Django 3.2 on 2021-04-29 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.DeleteModel(
            name='Notes',
        ),
    ]
