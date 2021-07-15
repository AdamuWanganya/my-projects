# Generated by Django 3.1 on 2020-08-17 01:27

from django.db import migrations, models
import django.db.models.deletion
import djangoerp.core.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
                ('title', models.CharField(blank=True, max_length=256, null=True, verbose_name='title')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'region',
                'verbose_name_plural': 'regions',
            },
        ),
        migrations.CreateModel(
            name='Plugget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('source', models.CharField(max_length=256, verbose_name='source')),
                ('template', models.CharField(default='pluggets/base_plugget.html', max_length=256, verbose_name='template')),
                ('context', models.TextField(blank=True, help_text='Use the JSON syntax.', null=True, validators=[djangoerp.core.models.validate_json], verbose_name='context')),
                ('sort_order', models.PositiveIntegerField(default=0, verbose_name='sort order')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pluggets', to='pluggets.region', verbose_name='region')),
            ],
            options={
                'verbose_name': 'plugget',
                'verbose_name_plural': 'pluggets',
                'ordering': ('region', 'sort_order', 'title'),
                'unique_together': {('region', 'title')},
            },
        ),
    ]