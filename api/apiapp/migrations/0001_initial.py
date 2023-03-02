# Generated by Django 3.2.18 on 2023-03-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Name')),
                ('last_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Surname')),
                ('tg_username', models.CharField(blank=True, max_length=256, null=True, verbose_name='username')),
                ('tg_id', models.BigIntegerField(unique=True, verbose_name='telegraam id')),
            ],
            options={
                'verbose_name': 'telegram user',
                'verbose_name_plural': 'telegram users',
            },
        ),
    ]