# Generated by Django 2.2.6 on 2019-10-04 12:53

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
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_profile_picture', models.CharField(default=None, max_length=500)),
                ('domicilio', models.CharField(default=None, max_length=100, null=True)),
                ('descripcion', models.CharField(default=None, max_length=250, null=True)),
                ('telefono', models.CharField(default=None, max_length=50, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
