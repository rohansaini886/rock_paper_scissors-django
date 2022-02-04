import http
from django.http import HttpResponse
from django.shortcuts import render
import random
def index(request):
    # return HttpResponse('hello world')
    return render(request, 'index.html')
def result(request):
    params = {}
    choosen = request.GET['choice']
    # print(choosen)
    comp = random.choices(["R", "P", "S"])
    device = comp[0]
    print(device)
    
    if device == choosen:
        params['result'] = "THIS GAME IS TIED." 
    if device == 'R':
        if choosen == 'P':
            params['result'] = "THIS GAME IS WON BY YOU."
        else:
            params['result'] = "THIS GAME IS WON BY COMPUTER."
    if device == 'S':
        if choosen == 'P':
            params['result'] = "THIS GAME IS WON BY COMPUTER."
        else:
            params['result'] = "THIS GAME IS WON BY YOU."
    if device == 'P':
        if choosen == "S":
            params['result'] = "THIS GAME IS WON BY YOU."
        else:
            params['result'] = "THIS GAME IS WON BY COMPUTER."
            
    return render(request, 'result.html', params)
