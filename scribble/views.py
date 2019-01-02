from django.shortcuts import render
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Index for POST
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'scribble/post_list.html', {'posts': posts})

# Index for COMMENT
def comments_list(request):
    posts = Comment.objects.all()
    return render(request, 'scribble/comment_list.html', {'comments': comments})

# Show for POST
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'scribble/post_detail.html', {'post': post})

# Show for COMMENT
def comment_detail(request, pk):
    comment = Comment.objects.get(id=pk)
    return render(request, 'scribble/comment_detail.html', {'comment': comment})

# Create for POST
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'scribble/post_form.html', {'form': form})

# Create for COMMENT
def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail', pk=comment.pk)
    else:
        form = CommentForm()
    return render(request, 'scribble/comment_form.html', {'form': form})

# Edit for POST
def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'scribble/post_form.html', {'form': form})

# Edit for COMMENT
def comment_edit(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail', pk=comment.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'scribble/comment_form.html', {'form': form})

# Delete for POST
def post_delete(request, pk):
    post.objects.get(id=pk).delete()
    return redirect('post_list')

# Delete for COMMENT
def comment_delete(request, pk):
    comment.objects.get(id=pk).delete()
    return redirect('comment_list')