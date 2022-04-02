from django.db import models

# Model for Table atbats
class Atbats(models.Model):
    ab_id = models.IntegerField(primary_key=True)
    batter_id = models.IntegerField(blank=True, null=True)
    event = models.CharField(max_length=20, blank=True, null=True)
    g_id = models.IntegerField(blank=True, null=True)
    inning = models.IntegerField(blank=True, null=True)
    o = models.IntegerField(blank=True, null=True)
    p_score = models.IntegerField(blank=True, null=True)
    p_throws = models.CharField(max_length=2, blank=True, null=True)
    pitcher_id = models.IntegerField(blank=True, null=True)
    stand = models.CharField(max_length=2, blank=True, null=True)
    top = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atbats'

# Model for Table pitches
class Pitches(models.Model):
    px = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    pz = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    start_speed = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    end_speed = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    spin_rate = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    spin_dir = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    break_angle = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    break_length = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    break_y = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    ax = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    ay = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    az = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    sz_bot = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    sz_top = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    type_confidence = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    vx0 = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    vy0 = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    vz0 = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    x = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    x0 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    y = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    y0 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    z0 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    pfx_x = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    pfx_z = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    nasty = models.IntegerField(blank=True, null=True)
    zone = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=3, blank=True, null=True)
    type = models.CharField(max_length=2, blank=True, null=True)
    pitch_type = models.CharField(max_length=3, blank=True, null=True)
    event_num = models.IntegerField(blank=True, null=True)
    b_score = models.IntegerField(blank=True, null=True)
    ab = models.ForeignKey(Atbats, models.DO_NOTHING, blank=True, null=True)
    b_count = models.IntegerField(blank=True, null=True)
    s_count = models.IntegerField(blank=True, null=True)
    outs = models.IntegerField(blank=True, null=True)
    pitch_num = models.IntegerField(blank=True, null=True)
    on_1b = models.IntegerField(blank=True, null=True)
    on_2b = models.IntegerField(blank=True, null=True)
    on_3b = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pitches'

### The below models are for auto-migrated Django tables (probably won't use) 
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PitchData(models.Model):
    ab_id = models.IntegerField()
    batter_id = models.IntegerField(blank=True, null=True)
    event = models.CharField(max_length=20, blank=True, null=True)
    g_id = models.IntegerField(blank=True, null=True)
    inning = models.IntegerField(blank=True, null=True)
    o = models.IntegerField(blank=True, null=True)
    p_score = models.IntegerField(blank=True, null=True)
    p_throws = models.CharField(max_length=2, blank=True, null=True)
    pitcher_id = models.IntegerField(blank=True, null=True)
    stand = models.CharField(max_length=2, blank=True, null=True)
    top = models.CharField(max_length=10, blank=True, null=True)
    px = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    pz = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    start_speed = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    end_speed = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    spin_rate = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    spin_dir = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    break_angle = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    break_length = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    break_y = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    ax = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    ay = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    az = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    sz_bot = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sz_top = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    type_confidence = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    vx0 = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    vy0 = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    vz0 = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    x = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    x0 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    y = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    y0 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    z0 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    pfx_x = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    pfx_z = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    nasty = models.IntegerField(blank=True, null=True)
    zone = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=3, blank=True, null=True)
    type = models.CharField(max_length=2, blank=True, null=True)
    pitch_type = models.CharField(max_length=3, blank=True, null=True)
    event_num = models.IntegerField(blank=True, null=True)
    b_score = models.IntegerField(blank=True, null=True)
    b_count = models.IntegerField(blank=True, null=True)
    s_count = models.IntegerField(blank=True, null=True)
    outs = models.IntegerField(blank=True, null=True)
    pitch_num = models.IntegerField(blank=True, null=True)
    on_1b = models.IntegerField(blank=True, null=True)
    on_2b = models.IntegerField(blank=True, null=True)
    on_3b = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pitch_data'

