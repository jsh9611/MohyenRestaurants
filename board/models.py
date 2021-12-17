from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
import os

# Create your models here.



# 카테고리 모델
class Category(models.Model):
    name = models.CharField(max_length = 50, unique = True) # 카테고리의 이름
    slug = models.SlugField(max_length = 200, unique = True, allow_unicode=True) # 슬러그 필드

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/board/category/{self.slug}/' # board/category/해당 슬러그값 url 반환

    class Meta:
        verbose_name_plural = 'Categories' # 카테고리의 이름이 Categories 로 나오도록 설정

# 포스트 모델
class Post(models.Model):
    title = models.CharField(max_length = 100) # 제목 필드
    content = MarkdownxField() # 내용 필드

    upload_image = models.ImageField(upload_to = 'blog/images/%Y/%m/%d/', blank = True) # 업로드 이미지 필드
    

    created_at = models.DateTimeField(auto_now_add=True) # 작성 날짜 필드 / 현재 시간으로 기록
    updated_at = models.DateTimeField(auto_now=True) # 수정 날짜 필드 / 현재 시간으로 기록

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) # 작성자 필드 / 삭제된 작성자는 None 으로 표시

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL) # 카테고리 필드 / 삭제된 카테고리는 None 으로 표시



    def __str__(self):
        return f'[{self.pk}]{self.title} / 작성자 : {self.author}' # 작성자 추가

    def get_absolute_url(self):
        return f'/board/{self.pk}/' # board 의 pk 값의 url 을 반환

    def get_file_name(self):
        return os.path.basename(self.file_upload.name) 

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

    def get_content_markdown(self):
        return markdown(self.content)

# 코멘트(댓글) 모델
class Comment(models.Model):
     post = models.ForeignKey(Post, on_delete=models.CASCADE) # 사용자가 삭제될 시 해당 사용자가 작성한 글도 같이 삭제한다.
     author = models.ForeignKey(User, on_delete=models.CASCADE)
     content = models.TextField()
     created_at = models.DateTimeField(auto_now_add = True)
     modified_at = models.DateTimeField(auto_now=True)

     def __str__(self):
         return f'{self.author}::{self.content}'

     def get_absolute_url(self):
         return f'{self.post.get_absolute_url()}#comment-{self.pk}' # board/{self.pk}#comment-{self.pk} 가 반환