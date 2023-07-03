from django.core.validators import (
    RegexValidator,
    MinValueValidator,
    MaxValueValidator,
)
from django.db import models

# Create your models here.
"""
First Name - Text box 50 char max
Last Name - Text box 50 char max
Email - Text box 100 char max
Mobile - Text box 10 char max number only
Age - 3 char max only number
Gender - Male / Female radio button - Single selection
Hobbies - Reading, Mussic, Movies - Checkbox multiple selection allowed
Bank - SBI, Maharashtra Bank, Punjab National bank (Single selection dropown)
Password - 8 characters - 1 Capital letter, 1 special character , 1 number must. Min 8 characters max 14 characters
"""


class Choice:
    GENDER = ((0, "Male"), (1, "Female"))
    HOBBIES = (
        ("Reading", "Reading"),
        ("Movies", "Movies"),
        ("Music", "Music"),
        ("Games", "Games"),
    )
    BANK = (
        ("SBI", "SBI"),
        ("RBI", "RBI"),
        ("PNB", "PNB"),
        ("Maharashtra Bank", "Maharashtra Bank"),
    )


class BankRegistration(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    age = models.IntegerField(
        default=1, validators=[MaxValueValidator(150), MinValueValidator(1)]
    )
    gender = models.IntegerField(choices=Choice.GENDER)
    hobbies = models.CharField(choices=Choice.HOBBIES, max_length=20)
    bank = models.CharField(choices=Choice.BANK, max_length=20)
    password = models.CharField(
        max_length=14,
        validators=[
            RegexValidator(
                regex="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",
                message="Password - 8 characters - 1 Capital letter, 1 special character , 1 number must. Min 8 characters max 14 characters",
                code="invalid password",
            ),
        ],
    )

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
