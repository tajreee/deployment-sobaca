# Generated by Django 4.2.6 on 2023-10-27 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20231026_1221'),
        ('discussion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussionthread',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book'),
        ),
    ]
