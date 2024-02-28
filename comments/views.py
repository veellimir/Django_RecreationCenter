from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Comments
from .forms import CommentsForm


def comment_user(request):
    profile = request.user.profile
    form = CommentsForm()
    existing_comment = Comments.objects.filter(owner=profile).exists()

    if existing_comment:
        return redirect('home')

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.owner = profile
            comments.save()
            messages.info(request, 'Благодарим за Ваш комментарий')
            return redirect('home')

    context = {
        'form': form,
        'existing_comment': existing_comment,
    }
    return render(request, 'mainapp/home.html', context)