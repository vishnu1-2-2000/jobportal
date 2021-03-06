# Generated by Django 4.0.4 on 2022-06-10 10:20

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
            name='Candidateprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='candidate')),
                ('resume', models.FileField(null=True, upload_to='cv')),
                ('qualification', models.CharField(max_length=120)),
                ('skills', models.CharField(max_length=120)),
                ('experience', models.PositiveIntegerField(default=0)),
                ('age', models.PositiveIntegerField(default=0)),
                ('location', models.CharField(max_length=120)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='candidate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
