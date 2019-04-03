# Generated by Django 2.1.5 on 2019-02-06 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_appointment', models.DateTimeField(verbose_name='Date of appointment')),
                ('complaints', models.TextField(verbose_name='Complaints')),
                ('diagnosis', models.TextField(verbose_name='Diagnosis')),
                ('care_plan', models.TextField(verbose_name='Care plan')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.IntegerField(default=0, verbose_name='patient ID')),
                ('patient_name', models.CharField(max_length=200, verbose_name='Name of patient')),
                ('patient_age', models.IntegerField(verbose_name='Age of patient')),
                ('date_registered', models.DateTimeField(verbose_name='Date of Registration')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.Patient'),
        ),
    ]