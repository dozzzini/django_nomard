from django.db import models
from common.models import CommonModel


# Create your models here.'
class Photo(CommonModel):
    file = models.ImageField()
    description = models.CharField(max_length=140)
    # 사진은 한 개의 방에만 종속됨
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )

    def __str__(self):
        return "Photo File"


# 비디오는 experience에만 종속되고 있음
class Video(CommonModel):
    file = models.FileField()
    experience = models.OneToOneField(
        "experiences.Experience",
        on_delete=models.CASCADE,  # 활동이 삭제되면 비디오도 삭제됨
        related_name="videos",
    )

    def __str__(self):
        return "Video File"
