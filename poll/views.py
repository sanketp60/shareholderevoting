from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Poll as PollModel
from .models import UserData as UserDataModel
from .models import Vote as VoteModel

def index(request):
    return render(request, 'poll/index.html')

def results(request):
    return render(request, 'poll/results.html')

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

@login_required(login_url='/login')
def vote_register(request):
    my_poll = PollModel.objects.get(PollID=request.POST['pollid'])
    my_user = User.objects.get(id=request.user.id)
    if request.POST['Decision']=='accept':
        vote = True
    else:
        vote = False
    my_vote = VoteModel.objects.create(User=my_user, Poll=my_poll, Feedback=vote)
    my_vote.save()
    return HttpResponse('Response Noted')