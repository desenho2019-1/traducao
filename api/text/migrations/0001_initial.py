# Generated by Django 2.1.7 on 2019-06-10 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
                ('category_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_username', models.CharField(max_length=50)),
                ('comment', models.TextField()),
                ('approve', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_fragments', models.IntegerField(default=0)),
                ('fragments_done', models.IntegerField(default=0)),
                ('fragments_revision', models.IntegerField(default=0)),
                ('fragments_doing', models.IntegerField(default=0)),
                ('context', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('language', models.IntegerField()),
                ('text_translate', models.TextField(blank=True, null=True)),
                ('categories', models.ManyToManyField(to='text.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TextFragment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('price', models.FloatField(default=0)),
                ('state', models.CharField(choices=[('1', 'To translate'), ('2', 'Translating'), ('3', 'To review'), ('4', 'Reviewing'), ('5', 'To finish'), ('6', 'Finished')], default='To translate', max_length=12)),
                ('total_reviews', models.IntegerField(default=0)),
                ('position', models.IntegerField(blank=True, null=True)),
                ('fragment_translate', models.TextField(blank=True, null=True)),
                ('fragment_translator', models.CharField(blank=True, max_length=50, null=True)),
                ('text', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='text.Text')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='review',
            name='fragment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='text.TextFragment'),
        ),
    ]
