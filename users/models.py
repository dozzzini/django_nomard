from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# AbstractUser을 상속받긴 하지만, 우리가 컨트롤할 수 있는 User라는 클래스를 생성함
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        # kr은 아래 설정했다시피 max_length가 2를 넘으면 안됨.
        # ("데이터베이스에서의 값", "관리자 페이지에서 볼 label")
        # Python에서 꼭 tuple을 사용하지 않아도 되기 때문에 ()는 생략 가능함.
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        WON = "won", "Korean Won"
        USD = "usd", "Dollar"

    # Abstractuser에 있는 속성들
    # editable = False를 해놓음으로서 관리자 페이지에서는 나타나지 않게 함
    first_name = models.CharField(("first name"), max_length=150, editable=False)
    last_name = models.CharField(("last name"), max_length=150, editable=False)
    # 내가 customize한 field
    # blank=True로 해준다면 form에서 필드를 비워놓을 수 있도록 해줌.
    avatar = models.ImageField(blank=True)
    # 새로 column을 생성한다면 이전의 user에게는 데이터의 default 값을 어떻게 줄 지 설정해야함
    name = models.CharField(max_length=150, default="")
    is_host = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
    )
    currency = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
    )
