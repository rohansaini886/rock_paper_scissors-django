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
    #print(device)
    
    if device == choosen:
        params['device'] = 'SAME AS YOU'
        params['result'] = "THIS GAME IS TIED 🤝." 
    elif device == 'R':
        params['device'] = 'ROCK'
        if device == choosen:
            params['result'] = "THIS GAME IS TIED 🤝."
        elif choosen == 'P':
            params['result'] = "THIS GAME IS WON BY YOU 😎."
        else:
            params['result'] = "THIS GAME IS WON BY COMPUTER 💻🖥."
    elif device == 'S':
        params['device'] = 'STONE'
        if device == choosen:
            params['result'] = "THIS GAME IS TIED 🤝."
        elif choosen == 'P':
            params['result'] = "THIS GAME IS WON BY COMPUTER 💻🖥."
        else:
            params['result'] = "THIS GAME IS WON BY YOU 😎."
    elif device == 'P':
        params['device'] = 'PAPER'
        if device == choosen:
            params['result'] = "THIS GAME IS TIED 🤝."
        elif choosen == "S":
            params['result'] = "THIS GAME IS WON BY YOU 😎."
        else:
            params['result'] = "THIS GAME IS WON BY COMPUTER 💻🖥."
            
    return render(request, 'result.html', params)
