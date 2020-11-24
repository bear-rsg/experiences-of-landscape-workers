# Generated by Django 3.1.3 on 2020-11-14 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('admin_published', models.BooleanField(default=True)),
                ('meta_created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('meta_lastupdated_datetime', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
            ],
        ),
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='journal.basemodel')),
                ('title', models.CharField(max_length=200)),
                ('entry_text', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Journal entries',
            },
            bases=('journal.basemodel',),
        ),
        migrations.CreateModel(
            name='JournalEntryAnalysisCode',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='journal.basemodel')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            bases=('journal.basemodel',),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='journal.basemodel')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('consent_message', models.TextField(blank=True, null=True)),
            ],
            bases=('journal.basemodel',),
        ),
        migrations.CreateModel(
            name='JournalEntryTag',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='journal.basemodel')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_public', models.BooleanField(default=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('journal.basemodel',),
        ),
        migrations.CreateModel(
            name='JournalEntryImage',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='journal.basemodel')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(upload_to='journalentryimages')),
                ('journal_entry', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='journal.journalentry')),
            ],
            bases=('journal.basemodel',),
        ),
        migrations.CreateModel(
            name='JournalEntryAnalysis',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='journal.basemodel')),
                ('analysis_text', models.TextField()),
                ('journal_entry', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='journal.journalentry')),
                ('journal_entry_analysis_code', models.ManyToManyField(blank=True, to='journal.JournalEntryAnalysisCode')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Journal entry analyses',
            },
            bases=('journal.basemodel',),
        ),
        migrations.AddField(
            model_name='journalentry',
            name='journal_entry_tag',
            field=models.ManyToManyField(blank=True, to='journal.JournalEntryTag'),
        ),
        migrations.AddField(
            model_name='journalentry',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]