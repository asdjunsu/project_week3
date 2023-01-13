from django.db import models


class Post(models.Model):
    # 데이터베이스의 필드(컬럼): 최대 길이가 30
    # title = models.CharField(max_length=30)
    # content = models.TextField()

    # created_at = models.DateTimeField()
    # author는 추후 작성
    # Create your models here.

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # 이름 , 이메일 , mbti, 사진, 자기소개
    name = models.CharField(max_length=10, blank=False, null=True, default="")
    email_address = models.EmailField(max_length=50, null=True)
    mbti = models.CharField(max_length=10, null=True, default="")
    # intro = models.TextField()
    content = models.TextField()
    introImage = models.ImageField(upload_to="blog/images/", blank=True)
    # profileImage = models.ImageField(upload_to="blog/images/", blank=True)

    # def __str__(self):
    #     return f"[{self.pk}] {self.title}, {self.created_at}"

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def __str__(self):
        return f"[{self.pk}] {self.name}"
