# Generated by Django 4.1.13 on 2024-05-09 03:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ops', '0001_initial'),
        ('assets', '0002_auto_20180105_1807'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='playbook',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='jobexecution',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='jobexecution',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='executions', to='ops.job'),
        ),
        migrations.AddField(
            model_name='job',
            name='assets',
            field=models.ManyToManyField(to='assets.asset', verbose_name='Assets'),
        ),
        migrations.AddField(
            model_name='job',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='job',
            name='playbook',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ops.playbook', verbose_name='Playbook'),
        ),
        migrations.AddField(
            model_name='historicaljob',
            name='creator',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='historicaljob',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaljob',
            name='playbook',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ops.playbook', verbose_name='Playbook'),
        ),
        migrations.AddField(
            model_name='celerytaskexecution',
            name='creator',
            field=models.ForeignKey(db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='adhoc',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AlterUniqueTogether(
            name='playbook',
            unique_together={('name', 'org_id', 'creator')},
        ),
        migrations.AlterUniqueTogether(
            name='job',
            unique_together={('name', 'org_id', 'creator')},
        ),
        migrations.AlterUniqueTogether(
            name='adhoc',
            unique_together={('name', 'org_id', 'creator')},
        ),
    ]
