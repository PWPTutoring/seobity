from django.shortcuts import render, redirect
from .models import Comment

def comment_view(request):
    if request.method == 'POST': 
        content = request.POST.get('content')
        Comment.objects.create(content=content)
        return redirect('comments:comment')

    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'comments/comment.html', {'comments': comments})




# from django.shortcuts import render

# def comment_view(request):
#     comment = None  
    
#     if request.method == 'POST':
#         comment = request.POST.get('comment_text')
        
        
#     return render(request, 'comments/comment.html', {'comment' : comment})
