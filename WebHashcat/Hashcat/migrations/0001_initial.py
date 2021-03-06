# Generated by Django 2.1.2 on 2019-02-17 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Nodes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_type', models.IntegerField()),
                ('username', models.CharField(max_length=190, null=True)),
                ('password', models.CharField(max_length=190, null=True)),
                ('hash', models.CharField(max_length=190, null=True)),
                ('password_len', models.IntegerField(null=True)),
                ('password_charset', models.CharField(max_length=100, null=True)),
                ('password_mask', models.CharField(max_length=190, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hashfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('hashfile', models.CharField(max_length=30)),
                ('hash_type', models.IntegerField()),
                ('line_count', models.IntegerField()),
                ('cracked_count', models.IntegerField(default=0)),
                ('username_included', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('output_lines', models.IntegerField(null=True)),
                ('output_file', models.TextField()),
                ('processing_time', models.IntegerField(null=True)),
                ('json_search_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('potfile_line_retrieved', models.IntegerField()),
                ('hashfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hashcat.Hashfile')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nodes.Node')),
            ],
        ),
        migrations.AddField(
            model_name='hash',
            name='hashfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hashcat.Hashfile'),
        ),
        migrations.AddIndex(
            model_name='hash',
            index=models.Index(fields=['hashfile'], name='hashfileid_index'),
        ),
        migrations.AddIndex(
            model_name='hash',
            index=models.Index(fields=['hashfile', 'hash'], name='hashfileid_hash_index'),
        ),
        migrations.AddIndex(
            model_name='hash',
            index=models.Index(fields=['hash', 'hash_type'], name='hash_index'),
        ),
    ]
