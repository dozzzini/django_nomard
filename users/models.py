from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    # AbstractUser을 상속받긴 하지만, 우리가 컨트롤할 수 있는 User라는 클래스를 생성함
    pass