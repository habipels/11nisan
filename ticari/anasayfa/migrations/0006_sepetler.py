# Generated by Django 3.2.13 on 2022-05-25 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anasayfa', '0005_rename_urun_urun_urun_aciklama'),
    ]

    operations = [
        migrations.CreateModel(
            name='sepetler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urunler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anasayfa.urun')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
