# Generated by Django 2.2.4 on 2019-10-29 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0002_auto_20191029_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dogbreed',
            name='FCI_group',
        ),
        migrations.AlterField(
            model_name='dog',
            name='age',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dogs.DogBreed'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='hair',
            field=models.CharField(choices=[('короткая шерсть', 'short'), ('длинная шерсть', 'long'), ('без шерсти', 'hairless')], default='короткая шерсть', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='photo',
            field=models.URLField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='dogbreed',
            name='hair',
            field=models.CharField(choices=[('короткая шерсть', 'short'), ('длинная шерсть', 'long'), ('без шерсти', 'hairless')], default='короткая шерсть', max_length=50),
        ),
        migrations.DeleteModel(
            name='FCIGroup',
        ),
    ]
