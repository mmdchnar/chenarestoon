from django.http import HttpResponse

def index(req):
    return HttpResponse('''
<p><b>Welcome to my site!</b></p>
<p><a href="/polls">Go to polls!</a></p>''')

