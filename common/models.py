from django.db import models

# Create your models here.
# 데이터베이스에는 저장하지 않고 다른 model에서 재사용을 하기 위해 만드는 model


class CommonModel(models.Model):
    # Common Model Definition

    # auto_now_add : 필드의 값을 해당 object가 처음 생성되었을 때의 시간으로 설정
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    # auto_now : object가 저장될 때마다 해당 필드의 현재 date로 설정
    updated_at = models.DateTimeField(auto_now=True)

    # common model에 대한 테이블을 만들지 않도록(데이터베이스에 보여지지 않게 하기 위해서) abstract model 사용
    class Meta:
        abstract = True
