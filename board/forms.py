from .models import Comment 
from django import forms
# models.py 의 Comment 모델 불러오고, django의 forms도 임포트한다.

# 댓글 작성 폼 구현
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)