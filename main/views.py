from django.shortcuts import render
from .models import Board, Output
import json
import requests
from django.http import JsonResponse, HttpResponse

def index(request):
    control = {}
    if request.method == 'POST':
        name = request.POST['name']
        board_id = request.POST['board_id']
        gpio = request.POST['gpio']
        state = request.POST['state']

        try:
            print('try')
            board = Board.objects.get(board=board_id)
            output = Output.objects.create(name=name,board=board, gpio=gpio, state=state)
            output.save()
        except:
            print('Failed')
            board = Board(board=board_id)
            board.save()
            output = Output.objects.create(name=name,board=board, gpio=gpio, state=state)
            output.save()


    control = Output.objects.all()
    print(control)
        
    return render(request, 'main/index.html', {'control': control})

def updatestate(request):
    output_id = request.GET.get('id')
    state = request.GET.get('state')
    counter = request.GET.get('counter')

    output = Output.objects.get(id=output_id)
    output.state = state
    output.save()

    print(output.state + ' now')
    req = requests.get('http://smarthometech.herokuapp.com/data/1')
    print(req)
    return JsonResponse({'state': state, 'id': output_id, 'counter': counter}, status=200)


def displayBoardData(request, board):
    output = Output.objects.filter(board=board)
    
    
    context = {}
    for o in output:
        context[o.gpio] = o.state
    str1 = json.dumps(context)
    return HttpResponse(str1)
    