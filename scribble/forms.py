from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'body',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'body', 'post',)


def post_create(request):
    if request.method == 'POST':
        form = postForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = postForm()
    return render(request, 'tunr/post_form.html', {'form': form})

def comment_create(request):
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail', pk=comment.pk)
    else:
        form = commentForm()
    return render(request, 'tunr/comment_form.html', {'form': form})