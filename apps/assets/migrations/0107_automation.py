# Generated by Django 3.2.16 on 2022-12-30 08:08

import common.db.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0106_auto_20221228_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseAutomation',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Comment')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('org_id', models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('is_periodic', models.BooleanField(default=False, verbose_name='Periodic perform')),
                ('interval', models.IntegerField(blank=True, default=24, null=True, verbose_name='Cycle perform')),
                ('crontab', models.CharField(blank=True, max_length=128, null=True, verbose_name='Regularly perform')),
                ('accounts', models.JSONField(default=list, verbose_name='Accounts')),
                ('type', models.CharField(max_length=16, verbose_name='Type')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('assets', models.ManyToManyField(blank=True, to='assets.Asset', verbose_name='Assets')),
                ('nodes', models.ManyToManyField(blank=True, to='assets.Node', verbose_name='Node')),
            ],
            options={
                'verbose_name': 'Automation task',
                'unique_together': {('org_id', 'name', 'type')},
            },
        ),
        migrations.CreateModel(
            name='AutomationExecution',
            fields=[
                ('org_id', models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('status', models.CharField(default='pending', max_length=16, verbose_name='Status')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('date_start', models.DateTimeField(db_index=True, null=True, verbose_name='Date start')),
                ('date_finished', models.DateTimeField(null=True, verbose_name='Date finished')),
                ('snapshot', common.db.fields.EncryptJsonDictTextField(blank=True, default=dict, null=True, verbose_name='Automation snapshot')),
                ('trigger', models.CharField(choices=[('manual', 'Manual trigger'), ('timing', 'Timing trigger')], default='manual', max_length=128, verbose_name='Trigger mode')),
                ('automation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='executions', to='assets.baseautomation', verbose_name='Automation task')),
            ],
            options={
                'verbose_name': 'Automation task execution',
                'ordering': ('-date_start',),
            },
        ),
        migrations.CreateModel(
            name='AssetBaseAutomation',
            fields=[
            ],
            options={
                'verbose_name': 'Asset automation task',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('assets.baseautomation',),
        ),
        migrations.CreateModel(
            name='GatherFactsAutomation',
            fields=[
                ('baseautomation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='assets.baseautomation')),
            ],
            options={
                'verbose_name': 'Gather asset facts',
            },
            bases=('assets.assetbaseautomation',),
        ),
        migrations.CreateModel(
            name='PingAutomation',
            fields=[
                ('baseautomation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='assets.baseautomation')),
            ],
            options={
                'verbose_name': 'Ping asset',
            },
            bases=('assets.assetbaseautomation',),
        ),
        migrations.AlterField(
            model_name='automationexecution',
            name='automation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='executions', to='assets.baseautomation', verbose_name='Automation task'),
        ),
    ]
