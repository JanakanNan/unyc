# Generated by Django 3.1.1 on 2020-11-02 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unycAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='raid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rankings', to='unycAPI.ranking'),
        ),
    ]