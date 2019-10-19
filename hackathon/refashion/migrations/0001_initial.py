# Generated by Django 2.2.6 on 2019-10-19 07:26

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('customer', 'Customer'), ('retailer', 'Retailer')], max_length=8)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('street', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('zip_code', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('donation_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('combined_weight', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Redemption',
            fields=[
                ('redemption_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('redemption_date_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('store_name', models.CharField(max_length=150)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='refashion.Address')),
            ],
        ),
        migrations.CreateModel(
            name='RewardRate',
            fields=[
                ('reward_rate_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('reward_multiplier', models.DecimalField(decimal_places=5, default=1, max_digits=7)),
                ('coupon_code', models.CharField(max_length=150)),
                ('test', models.CharField(max_length=150)),
                ('donation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='refashion.Donation')),
            ],
        ),
        migrations.CreateModel(
            name='Retailer',
            fields=[
                ('retailer_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='refashion.Address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
