from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Homestay(models.Model):
    title = models.CharField(max_length=35)
    description = models.TextField(max_length=100)
    address = models.CharField('Address', max_length=300)
    score = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)], null=True)
    main_image = models.ImageField(upload_to='images/', null=True)
    homestay_dot_com_id = models.PositiveIntegerField(unique=True, null=True)

    # Facilities
    facilities = models.ManyToManyField('Facility', symmetrical=False)

    # Meals

    light_breakfast = models.BooleanField('Complimentary Light Breakfast')
    use_of_kitchen = models.BooleanField('Use of Kitchen')

    # House Rule

    rules = models.CharField('House rules', max_length=300)

    # Address

    address_lat = models.FloatField()
    address_lng = models.FloatField()
    about_area = models.TextField()


    #
    # preferred_length_min = models.PositiveSmallIntegerField()
    # preferred_length_max = models.PositiveSmallIntegerField()
    #
    # currency = models.CharField()
    #
    # # Meals
    # use_kitchen = models.BooleanField()
    # provide_meals = models.BooleanField()
    #
    # rule = models.CharField()
    # family_smoke = models.BooleanField()
    # guest_smoke = models.BooleanField()

    def __str__(self):
        return self.title


#
# class Price(models.Model):
#     include_light_breakfast = models.BooleanField()


# class Room(models.Model):
#     bedroom_name = models.CharField()
#     beds = models.PositiveSmallIntegerField()
#     num_guest = models.PositiveSmallIntegerField()
#     bathroom_type = models.SmallIntegerField()
#     # Ensuit (within room)
#     # Shared (with family/ other guests)
#     # Private (exclusive to guest)


# class Address(models.Model):
#     country = models.CharField("Country")
#     city = models.CharField("City/Town")
#     address_line1 = models.CharField()
#     address_line2 = models.CharField()
#     area = models.CharField("Neighbourhood/Area")
#     state = models.CharField('State/County')
#     postcode = models.PositiveIntegerField('Postcode/Zip')
#     about = models.CharField(validators=MinLengthValidator(100))
#     facilities = models.ManyToManyField('Facility', symmetrical=False)


# class Contract(models.Model):
#     class State(models.IntegerChoices):
#         NEW = 1  # Đã đặt cọc nhưng chưa bắt đầu
#         RUNNING = 2  # Đang sử dụng
#         FINISHED = 3  # Hoàn thành
#         CANCELED = -1  # Bị hủy
#

class Facility(models.Model):
    name = models.CharField(max_length=20, unique=True)
    address_facility = models.BooleanField()

    def __str__(self):
        return self.name


class ReviewImage(models.Model):
    image = models.ImageField(unique=True, upload_to='image/review_images')
    homestay = models.ForeignKey(Homestay, on_delete=models.CASCADE, max_length=400)
