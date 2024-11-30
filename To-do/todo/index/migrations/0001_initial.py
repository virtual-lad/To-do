# Generated by Django 5.1.2 on 2024-11-28 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
