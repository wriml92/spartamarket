from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
import re

# 상품 이미지를 저장할 경로를 생성하는 함수
def product_image_path(instance, filename):
    return f'product_images/{instance.user.username}/{filename}'

# 파이썬의 정규표현식
# 해시태그가 유효한지 검사하는 사용자 정의 함수를 선언(해시태그는 띄어쓰기와 특수문자가 허용되지 않습니다.)
def validation_hastag(value):
    # 정규표현식 -> 공백 / 특수문자를 불허하는 코드입니다.
    if not re.match(r'^[0-9a-zA-Z_]+$', value):
        raise ValidationError('해시태그는 알파벳, 숫자, 언더스코어만 가능합니다~!')

# 해시태그를 저장하는 모델이다~
class HashTag(models.Model):
    name = models.CharField(max_length=50, unique=True, validators=[validation_hastag])

    def __str__(self):
        return f'#{self.name}'
    
# 사용자의 등록한 상품을 저장하는 모델
class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=product_image_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # 사용자가 상품에 '좋아요'를 누를 수 있도록 하잖아요! (그런 관계)
    # user like (좋아요는) 어떤 관계일까요? -> ManyToManyField 다대다 관계를 설정 가능(User 모델이랑)
    # 상품에 좋아요가 없을 수도 있어요 blank = True
    # 사용자가 좋아요를 누른 상품을 user.liked_products 참조 가능하다 -> 상품을 주르륵 나옵니다(리스트가)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_products', blank=True)
    # 상품에 연결되어 있는 해시태그
    # 다대다 관계
    hashtags = models.ManyToManyField(HashTag, related_name='products', blank=True)
    # 상품의 조회수
    views = models.PositiveIntegerField(default=0)

    def like_count(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title