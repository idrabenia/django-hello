from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect

from .models import User
from .forms import UserForm


def index(request):
    return render(request, 'list_users.html', {'users': User.objects.all()})


def user_details(request, user_id):
    cur_user = get_object_or_404(User, pk=user_id)

    return render(request, 'user_details.html', {'cur_user': cur_user})


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.create(**form.cleaned_data)

            return redirect(reverse('users:details', args=[user.id]))
    else:
        form = UserForm()

    return render(request, 'user_form.html', {'form': form})