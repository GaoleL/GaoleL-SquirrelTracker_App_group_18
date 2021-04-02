# Generated by Django 3.1.7 on 2021-04-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('X', models.FloatField(help_text='Longitude')),
                ('Y', models.FloatField(help_text='Latitude')),
                ('Unique_squirrel_id', models.CharField(help_text='Unique Squirrel ID', max_length=100)),
                ('Shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], help_text='Shift Choices', max_length=100)),
                ('Date', models.DateField(help_text='Date')),
                ('Age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], max_length=100)),
                ('Primary_Fur_Color', models.CharField(blank=True, choices=[('Grey', 'Grey'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], help_text='Primary Fur Color', max_length=100)),
                ('Location', models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], help_text='location', max_length=100)),
                ('Specific_location', models.CharField(blank=True, help_text='Specific Location', max_length=100)),
                ('Running', models.BooleanField(help_text='running', max_length=100)),
                ('Chasing', models.BooleanField(help_text='chasing', max_length=100)),
                ('Climbing', models.BooleanField(help_text='climbing', max_length=100)),
                ('Eating', models.BooleanField(help_text='eating', max_length=100)),
                ('Foraging', models.BooleanField(help_text='foraging', max_length=100)),
                ('Other_activities', models.CharField(blank=True, help_text='other activities', max_length=100)),
                ('Kuks', models.BooleanField(help_text='kukking', max_length=100)),
                ('Quaas', models.BooleanField(help_text='quaaing', max_length=100)),
                ('Moans', models.BooleanField(help_text='moaning', max_length=100)),
                ('Tail_flags', models.BooleanField(help_text='Tail flagging', max_length=100)),
                ('Tail_twitches', models.BooleanField(help_text='Tail twitching', max_length=100)),
                ('Approaches', models.BooleanField(help_text='approaching', max_length=100)),
                ('Indifferent', models.BooleanField(help_text='indifferent', max_length=100)),
                ('Runs_From', models.BooleanField(help_text='running from humans', max_length=100)),
            ],
        ),
    ]
