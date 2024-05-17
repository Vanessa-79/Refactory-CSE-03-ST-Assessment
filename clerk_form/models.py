from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from datetime import date
import re  
# Create your models here.


def validate_letters(value):
    if not re.match("^([a-zA-Z]+\s)*[a-zA-Z]+$", value):
        raise ValidationError("Only letters are allowed.")


def validate_age(value):
    today = date.today()
    age = today.year - value.year - \
        ((today.month, today.day) < (value.month, value.day))
    if age < 18:
        raise ValidationError(_('You must be at least 18 years old and above.'))


class Userform(models.Model):
    GENDER = [
      ('', '--select--'),
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    first_name = models.CharField(max_length=50,
                                  validators=[MinLengthValidator(4), validate_letters])
    last_name = models.CharField(max_length=50,
                                 validators=[MinLengthValidator(4), validate_letters])
    course = models.CharField(max_length=255, choices=(

        ('', '--select--'),
        ('Certificate in Health Science', 'Certificate in Health Science'),
        ('Certificate in Applied Technology', 'Certificate in Applied Technology'),
        ('Bachelor of Information Technology', 'Bachelor of Information Technology'),
        ('Bachelors in Business Technology', 'Bachelors in Business Technology'),
        ('Master of Public Health', 'Master of Public Health')))


    entry_scheme = models.CharField(max_length=255, choices= (
         ('', '--select--'),
        ('A-Level certificate', 'A-Level certificate'),
        ('Adult/Mature Learning', 'Adult/Mature Learning'),
        ('Certificate', 'Certificate'),
        ('Diploma', 'Diploma'),
        ('Bachelors', 'Bachelors')))
    
    intake = models.CharField(max_length=255, choices= (
         ('', '--select--'),
        ('January Intake', 'January Intake'),
        ('May Intake', 'May Intake'),
        ('Certificate', 'Certificate'),
        ('August Intake', 'August Intake')))
      
    sponsorship = models.CharField(max_length=100, choices= (
         ('', '--select--'),
        ('Private', 'Private'),
        ('Government', 'Government'),
        ('Bursary', 'Bursary')))
    gender = models.CharField(max_length=100, choices=GENDER)
    date_of_birth = models.DateField(validators=[validate_age])
    residence =  models.CharField(max_length=255,
                                  validators=[MinLengthValidator(3), validate_letters])
    



    def clean(self):
        # If you want to perform additional model-level validation, you can do it here
        super().clean()


    def __str__(self):
        return self.first_name
