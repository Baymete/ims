from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from inventory.forms import UsersForm

# def users(request):
#     if request.method == 'POST':
#         form = UsersForm(request.POST)
#         if form.is_valid():
#             pass
#     else:
#         user_list = User.objects.all()
#         form = UsersForm()
#         return render(request,'users.html', {'form': form })