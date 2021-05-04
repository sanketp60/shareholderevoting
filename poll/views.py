from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Poll as PollModel
from .models import UserData as UserDataModel
from .models import Vote as VoteModel
from .models import UserCompanyMapper as UserCompanyMapperModel

def index(request):
    return render(request, 'poll/index.html')

def results(request, pollid):
    my_poll = PollModel.objects.get(PollID=pollid)
    if my_poll.ResultDateTime >= timezone.now():
        show_result = False
    else:
        show_result = True
    yes_votes = VoteModel.objects.filter(Poll=my_poll, Feedback=True).count()
    no_votes = VoteModel.objects.filter(Poll=my_poll, Feedback=False).count()
    context = {
        'yes_votes': yes_votes, 
        'no_votes': no_votes, 
        'company_name': my_poll.Company.Name, 
        'poll_content': my_poll.Content,
        'show_result': show_result,
        'result_datetime': my_poll.ResultDateTime
        }
    return render(request, 'poll/results.html', context)

@login_required(login_url='/login')
def vote(request, pollid):
    user_data = User.objects.get(id=request.user.id)
    my_poll = PollModel.objects.get(PollID=pollid)
    x = UserCompanyMapperModel.objects.filter(User=user_data, Company=my_poll.Company).count()
    if x == 1:
        allow_to_vote = True
    else:
        allow_to_vote = False
    if VoteModel.objects.filter(User=user_data, Poll=my_poll).count():
        already_vote = 1
    else:
        already_vote = 0
    context = {
        'my_poll': my_poll, 
        'already_vote': already_vote,
        'allow_to_vote': allow_to_vote
        }
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