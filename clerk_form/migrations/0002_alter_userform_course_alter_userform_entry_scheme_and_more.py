# Generated by Django 4.2.11 on 2024-05-17 09:36

import clerk_form.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clerk_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userform',
            name='course',
            field=models.CharField(choices=[('Certificate in Health Science', 'Certificate in Health Science'), ('Certificate in Applied Technology', 'Certificate in Applied Technology'), ('Bachelor of Information Technology', 'Bachelor of Information Technology'), ('Bachelors in Business Technology', 'Bachelors in Business Technology'), ('Master of Public Health', 'Master of Public Health')], max_length=255),
        ),
        migrations.AlterField(
            model_name='userform',
            name='entry_scheme',
            field=models.CharField(choices=[('A-Level certificate', 'A-Level certificate'), ('Adult/Mature Learning', 'Adult/Mature Learning'), ('Certificate', 'Certificate'), ('Diploma', 'Diploma'), ('Bachelors', 'Bachelors')], max_length=255),
        ),
        migrations.AlterField(
            model_name='userform',
            name='first_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(4), clerk_form.models.validate_letters]),
        ),
        migrations.AlterField(
            model_name='userform',
            name='intake',
            field=models.CharField(choices=[('January Intake', 'January Intake'), ('May Intake', 'May Intake'), ('Certificate', 'Certificate'), ('August Intake', 'August Intake')], max_length=255),
        ),
        migrations.AlterField(
            model_name='userform',
            name='last_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(4), clerk_form.models.validate_letters]),
        ),
        migrations.AlterField(
            model_name='userform',
            name='residence',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(3), clerk_form.models.validate_letters]),
        ),
        migrations.AlterField(
            model_name='userform',
            name='sponsorship',
            field=models.CharField(choices=[('Private', 'Private'), ('Government', 'Government'), ('Bursary', 'Bursary')], max_length=100),
        ),
    ]