from django.shortcuts import render, redirect
from .models import Comments
from .forms import CommentsForm


def comment_user(request):
    profile = request.user.profile
    form = CommentsForm()

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.owner = profile
            comments.save()

            return redirect('home')

    return render(request, 'mainapp/home.html', {'form': form})
