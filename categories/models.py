from django.db import models
from common.models import CommonModel

# Create your models here.


class Category(CommonModel):
    # room or experience category

    class CategoryKindChoices(models.TextChoices):
        ROOMS = "rooms", "Rooms"
        EXPERIENCES = "experiences", "Experiences"

    name = models.CharField(max_length=50)
    kind = models.CharField(
        max_length=15,
        choices=CategoryKindChoices.choices,
    )

    def __str__(self) -> str:
        return (
            f"{self.kind.title()}:{self.name}"  # .title() 문자열의 첫번째 글자를 대문자로 바꿔주는 method
        )

    class Meta:
        verbose_name_plural = "Categories"
