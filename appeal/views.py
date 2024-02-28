from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def appeal_page(request):
    profile = request.user.profile
    message_request = profile.messages.all()

    count_msg = message_request.filter(is_read=False).count()

    context = {
        'message_request': message_request,
        'count_msg': count_msg
    }
    return render(request, 'appeal/chat.html', context)


@login_required(login_url='login')
def appeal_views(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)

    if message.is_read is False:
        message.is_read = True
        message.save()

    context = {
        'message': message
    }
    return render(request, 'appeal/view_message.html', context)