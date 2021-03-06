from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import JSONEncoder
from web.models import Income, Expense, Token, User
from datetime import datetime
# Create your views here.

@csrf_exempt
def submit_income(request):
    this_token = request.POST['token']
    if 'date' not in request.POST:
        date = datetime.now()
    this_user = User.objects.filter(token__token=this_token).get()
    Income.objects.create(user=this_user, amount=request.POST['amount'],
                           text=request.POST['text'], date=date)

    return JsonResponse({
        'status': 'ok'
    }, encoder=JSONEncoder)


@csrf_exempt
def submit_expense(request):
    this_token = request.POST['token']
    if 'date' not in request.POST:
        date = datetime.now()
    this_user = User.objects.filter(token__token=this_token).get()
    Expense.objects.create(user=this_user, amount=request.POST['amount'],
                           text=request.POST['text'], date=date)

    return JsonResponse({
        'status': 'ok'
    }, encoder=JSONEncoder)