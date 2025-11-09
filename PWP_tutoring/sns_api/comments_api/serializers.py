from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at']
        read_only_fields = ['id', 'created_at']

class CommentCreateSerializer(serializers.ModelSerializer):
    content = serializers.CharField(
        max_length=500,
        min_length=1,
        error_messages={
            'required': '댓글 내용은 필수입니다.',
            'blank': '댓글 내용을 입력해주세요.',
            'max_length': '댓글은 500자 이내로 작성해주세요.',
        }
    )

    class Meta:
        model = Comment
        fields = ['content']