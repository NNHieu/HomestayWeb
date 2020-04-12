from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class Facility(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    description = models.CharField()


class Homestay(models.Model):
    address = models.CharField(max_length=200)

    class Type(models.IntegerChoices):
        APARTMENT = 1
        HOUSE = 2

    type = models.SmallIntegerField(choices=Type.choices)
    title = models.CharField(max_length=35)
    description = models.TextField(validators=MinLengthValidator(100))
    facilities = models.ManyToManyField('Facility', symmetrical=False)

    preferred_length_min = models.PositiveSmallIntegerField()
    preferred_length_max = models.PositiveSmallIntegerField()

    currency = models.CharField()

    # Meals
    use_kitchen = models.BooleanField()
    provide_meals = models.BooleanField()

    rule = models.CharField()
    family_smoke = models.BooleanField()
    guest_smoke = models.BooleanField()


class Price(models.Model):
    include_light_breakfast = models.BooleanField()


class Room(models.Model):
    bedroom_name = models.CharField()
    beds = models.PositiveSmallIntegerField()
    num_guest = models.PositiveSmallIntegerField()
    bathroom_type = models.SmallIntegerField()
    # Ensuit (within room)
    # Shared (with family/ other guests)
    # Private (exclusive to guest)


class Address(models.Model):
    country = models.CharField("Country")
    city = models.CharField("City/Town")
    address_line1 = models.CharField()
    address_line2 = models.CharField()
    area = models.CharField("Neighbourhood/Area")
    state = models.CharField('State/County')
    postcode = models.PositiveIntegerField('Postcode/Zip')
    about = models.CharField(validators=MinLengthValidator(100))
    facilities = models.ManyToManyField('Facility', symmetrical=False)


class Contract(models.Model):
    class State(models.IntegerChoices):
        NEW = 1  # Đã đặt cọc nhưng chưa bắt đầu
        RUNNING = 2  # Đang sử dụng
        FINISHED = 3  # Hoàn thành
        CANCELED = -1  # Bị hủy
