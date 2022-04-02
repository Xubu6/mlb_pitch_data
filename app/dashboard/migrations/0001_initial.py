# Generated by Django 4.0.2 on 2022-04-02 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atbats',
            fields=[
                ('ab_id', models.IntegerField(primary_key=True, serialize=False)),
                ('batter_id', models.IntegerField(blank=True, null=True)),
                ('event', models.CharField(blank=True, max_length=20, null=True)),
                ('g_id', models.IntegerField(blank=True, null=True)),
                ('inning', models.IntegerField(blank=True, null=True)),
                ('o', models.IntegerField(blank=True, null=True)),
                ('p_score', models.IntegerField(blank=True, null=True)),
                ('p_throws', models.CharField(blank=True, max_length=2, null=True)),
                ('pitcher_id', models.IntegerField(blank=True, null=True)),
                ('stand', models.CharField(blank=True, max_length=2, null=True)),
                ('top', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'atbats',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PitchData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ab_id', models.IntegerField()),
                ('batter_id', models.IntegerField(blank=True, null=True)),
                ('event', models.CharField(blank=True, max_length=20, null=True)),
                ('g_id', models.IntegerField(blank=True, null=True)),
                ('inning', models.IntegerField(blank=True, null=True)),
                ('o', models.IntegerField(blank=True, null=True)),
                ('p_score', models.IntegerField(blank=True, null=True)),
                ('p_throws', models.CharField(blank=True, max_length=2, null=True)),
                ('pitcher_id', models.IntegerField(blank=True, null=True)),
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
                ('ax', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('ay', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('az', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('sz_bot', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('sz_top', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('type_confidence', models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)),
                ('vx0', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('vy0', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('vz0', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('x', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('x0', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('y', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('y0', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('z0', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('pfx_x', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('pfx_z', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('nasty', models.IntegerField(blank=True, null=True)),
                ('zone', models.IntegerField(blank=True, null=True)),
                ('code', models.CharField(blank=True, max_length=3, null=True)),
                ('type', models.CharField(blank=True, max_length=2, null=True)),
                ('pitch_type', models.CharField(blank=True, max_length=3, null=True)),
                ('event_num', models.IntegerField(blank=True, null=True)),
                ('b_score', models.IntegerField(blank=True, null=True)),
                ('b_count', models.IntegerField(blank=True, null=True)),
                ('s_count', models.IntegerField(blank=True, null=True)),
                ('outs', models.IntegerField(blank=True, null=True)),
                ('pitch_num', models.IntegerField(blank=True, null=True)),
                ('on_1b', models.IntegerField(blank=True, null=True)),
                ('on_2b', models.IntegerField(blank=True, null=True)),
                ('on_3b', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pitch_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pitches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('px', models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)),
                ('pz', models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)),
                ('start_speed', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('end_speed', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('spin_rate', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('spin_dir', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('break_angle', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('break_length', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('break_y', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('ax', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('ay', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('az', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('sz_bot', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('sz_top', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('type_confidence', models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)),
                ('vx0', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('vy0', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('vz0', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('x', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('x0', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('y', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('y0', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('z0', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('pfx_x', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('pfx_z', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('nasty', models.IntegerField(blank=True, null=True)),
                ('zone', models.IntegerField(blank=True, null=True)),
                ('code', models.CharField(blank=True, max_length=3, null=True)),
                ('type', models.CharField(blank=True, max_length=2, null=True)),
                ('pitch_type', models.CharField(blank=True, max_length=3, null=True)),
                ('event_num', models.IntegerField(blank=True, null=True)),
                ('b_score', models.IntegerField(blank=True, null=True)),
                ('b_count', models.IntegerField(blank=True, null=True)),
                ('s_count', models.IntegerField(blank=True, null=True)),
                ('outs', models.IntegerField(blank=True, null=True)),
                ('pitch_num', models.IntegerField(blank=True, null=True)),
                ('on_1b', models.IntegerField(blank=True, null=True)),
                ('on_2b', models.IntegerField(blank=True, null=True)),
                ('on_3b', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pitches',
                'managed': False,
            },
        ),
    ]
