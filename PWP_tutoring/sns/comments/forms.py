from django import forms
from .models import Comment
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={
                'placeholder': '댓글을 입력하세요',
                'class': 'comment-input'
            })
        }

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 2:
            raise forms.ValidationError('댓글은 2글자 이상이어야 합니다.')
        if '욕설' in content:
            raise forms.ValidationError('부적절한 단어가 포함되어 있습니다.')
        return content
    
class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='비밀번호 확인')

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
