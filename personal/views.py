from django.shortcuts import render
from personal.forms import Res

def index(request):
    return render(request, 'personal/FL.html')
def reserve(request):
    if(request.method=="POST"):
        pass

    else:
        form = Res()
        args = {'forms': form}
        return render(request, 'personal/R.html', args)
