from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'calci/index.html')

def calculate(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        operation = request.POST.get('operation')
        
        if operation == 'ADD':
            result = num1 + num2
        elif operation == 'SUB':
            result = num1 - num2
        elif operation == 'MUL':
            result = num1 * num2
        elif operation == 'DIV':
            result = num1 / num2
        return render(request, 'calci/index.html', {'result':result})
    return HttpResponse("Invalid Request")
        
    