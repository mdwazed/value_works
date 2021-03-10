from django.http import HttpResponse


def index_view(request):
    """ index view to test request response cycle """
    return HttpResponse('Index view')