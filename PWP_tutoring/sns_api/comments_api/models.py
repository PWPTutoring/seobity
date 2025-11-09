from django.db import models

class Comment(models.Model):
    content = models.TextField(verbose_name='댓글 내용')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일시')

    class Meta:
        db_table = 'comments'
        ordering = ['-created_at']

    def str(self):
        return f"{self.content[:30]}"