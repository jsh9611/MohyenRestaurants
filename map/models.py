from django.db import models
class Restaurants(models.Model):
    id = models.AutoField(primary_key=True)     # id
    name = models.CharField(max_length=20)      # 구 이름
    kinds = models.CharField(max_length=20)     # 도로명
    score = models.FloatField()                 # 별점
    review = models.CharField(max_length=20)    # 리뷰 수
    web_link = models.CharField(max_length=200) # 웹페이지 주소
    address = models.CharField(max_length=200)  # 음식점 주소
    lat = models.FloatField()                   # 위도
    lng = models.FloatField()                   # 경도
    category = models.CharField(max_length=20)  # 음식점 카테고리