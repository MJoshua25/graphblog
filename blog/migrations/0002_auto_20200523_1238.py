# Generated by Django 2.2.8 on 2020-05-23 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentaire',
            name='email',
        ),
        migrations.RemoveField(
            model_name='commentaire',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='commentaire',
            name='prenom',
        ),
        migrations.AddField(
            model_name='categorie',
            name='titre_slug',
            field=models.SlugField(editable=False, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='titre_slug',
            field=models.SlugField(editable=False, max_length=255, null=True),
        ),
    ]