# Generated by Django 4.1.10 on 2023-11-16 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_gatheraccountsautomation_recipients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountbackupautomation',
            name='backup_type',
            field=models.CharField(choices=[('email', 'Email'), ('object_storage', 'SFTP')], default='email', max_length=128, verbose_name='Backup Type'),
        ),
        migrations.AlterField(
            model_name='accountbackupautomation',
            name='is_password_divided_by_email',
            field=models.BooleanField(default=True, verbose_name='Is Password Divided'),
        ),
        migrations.AlterField(
            model_name='accountbackupautomation',
            name='is_password_divided_by_obj_storage',
            field=models.BooleanField(default=True, verbose_name='Is Password Divided'),
        ),
    ]
