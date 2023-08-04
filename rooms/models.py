from django.db import models
from common.models import CommonModel


# Create your models here.
class Room(CommonModel):
    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private room", "Private Room")
        SHARED_ROOM = ("shared room", "Shared Room")

    # Room Model Definition\
    name = models.CharField(
        max_length=180,
        default="",
    )
    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pet_friendly = models.BooleanField(default=True)
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    amenities = models.ManyToManyField(
        "rooms.Amenity",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    # Room에서 object 형식이 아니라 string 형식으로 나타내줌.
    def __str__(self) -> str:
        return self.name


class Amenity(CommonModel):
    # Amenity Definition
    name = models.CharField(max_length=150)
    description = models.CharField(
        max_length=150,
        null=True,  # 필드가 데이터베이스에서 null 가능
        blank=True,  # 장고 form 에서의 공백
    )

    # Amenity에서 object 형식이 아니라 string 형식으로 나타내줌.
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
