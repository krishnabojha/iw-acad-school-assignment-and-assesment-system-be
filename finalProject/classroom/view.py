from djanfo.http import HttpResponse

def index(request):
    return HttpResponse('from index')