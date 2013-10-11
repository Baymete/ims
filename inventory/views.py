from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from inventory.models import ItemHistory
 
def item_history(request, id):
    history_log = ItemHistory.objects.filter(item__id=id)
    return render_to_response('itemhistory.html', {'history_log': history_log } )

def users(request):
    users = User.objects.all()
    return render_to_response('users.html', {'users': users})

def main(request):
    return render_to_response('main.html')