from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm, SignUpForm

def comment_view(request):
    if request.method == 'POST': 
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comments:comment')
    else:
        form = CommentForm()

    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'comments/comment.html', {
        'form': form,
        'comments': comments
    })

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('comments:comment')
    else:
        form = SignUpForm()

    return render(request, 'comments/signup.html', {'form': form})