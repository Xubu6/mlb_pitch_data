# Generated by Django 4.0.2 on 2022-04-27 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_playernames'),
    ]

    operations = [
        migrations.CreateModel(
            name='PitchAnalysisView',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ab_id', models.IntegerField()),
                ('batter_id', models.IntegerField(blank=True, null=True)),
                ('batter_name', models.CharField(blank=True, max_length=55, null=True)),
                ('event', models.CharField(blank=True, max_length=20, null=True)),
                ('pitcher_id', models.IntegerField(blank=True, null=True)),
                ('pitcher_name', models.CharField(blank=True, max_length=55, null=True)),
                ('stand', models.CharField(blank=True, max_length=2, null=True)),
                ('top', models.CharField(blank=True, max_length=10, null=True)),
                ('px', models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)),
                ('pz', models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)),
                ('start_speed', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('end_speed', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('spin_rate', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('spin_dir', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('break_angle', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('break_length', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('break_y', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('nasty', models.IntegerField(blank=True, null=True)),
                ('zone', models.IntegerField(blank=True, null=True)),
                ('code', models.CharField(blank=True, max_length=3, null=True)),
                ('type', models.CharField(blank=True, max_length=2, null=True)),
                ('pitch_type', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'db_table': 'pitch_analysis_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PitcherInfo',
            fields=[
                ('pitcher_name', models.CharField(max_length=55, primary_key=True, serialize=False)),
                ('avg_start_speed', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('avg_spin_rate', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('avg_break_length', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('avg_break_y', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'pitcher_info',
                'managed': False,
            },
        ),
    ]
