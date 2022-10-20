from django.db import models

# Create your models here.
class Coffee(models.Model):
    # Field 1 -> 각 column을 의미
    # field1 = model.FieldType() 꼴
    # fieldtype에는 문자열, 숫자, 논리형, 시간/날짜 등이 있다
    def __str__(self):
        return self.name
    name = models.CharField(default = '', max_length = 30, null = False)
    price = models.IntegerField(default = 0)
    is_ice = models.BooleanField(default = False)