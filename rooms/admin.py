from django.contrib import admin
from .models import Room, Amenity


@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()


# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions = (reset_prices,)

    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",  # room 안에 들어있는 amenities의 갯수
        "rating",
        "owner",
        "created_at",
    )

    # 이 method를 관리자 패널에 넣는 방법
    def total_amenities(
        self, room
    ):  # models.py에 쓴 것처럼 self만 쓰게 되면, self가 가리키는 것은 RoomAdmin이다.
        # RoomAdmin의 매개변수인 room도 가져오게 하고 싶기 때문에 self, room 둘 다 작성해야한다.
        print(room)
        return "hellow"

    list_filter = (
        "country",
        "city",
        "rooms",
        "toilets",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "name",
        "^price",
        "owner__username",
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
