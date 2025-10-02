from django.shortcuts import render

def comment_view(request):
    comment = None  
    
    if request.method == 'POST':
        comment = request.POST.get('comment_text')
        
        
    return render(request, 'comments/comment.html', {'comment' : comment})
