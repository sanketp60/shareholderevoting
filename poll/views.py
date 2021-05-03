from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Poll as PollModel
from .models import UserData as UserDataModel

def index(request):
    return render(request, 'poll/index.html')

@login_required(login_url='/login')
def vote(request, pollid):
    my_poll = PollModel.objects.get(PollID=pollid)
    context = {'my_poll': my_poll}
    print(context)
    return render(request, 'poll/vote.html', context)

@login_required(login_url='/login')
def profile(request):
    user_data = User.objects.get(id=request.user.id)
    user_additional_data = UserDataModel.objects.get(UserID=user_data)
    context = {'user_data': user_data, 'user_additional_data': user_additional_data}
    return render(request, 'poll/profile.html', context)