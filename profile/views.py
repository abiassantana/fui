from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user.models import User_animal
from django.contrib.auth.decorators import login_required
from profile.forms import edit_photo_form
from user.forms import usuario_form
from user import urls
# Create your views here.

@login_required
def profile(request):
    form = edit_photo_form()
    user = request.user
    user_animal = User_animal.objects.get(user=user.id)
    if user_animal.type == 'Animal':
        return render(request, 'profile/profile_animal.html', { 'user_animal':user_animal, 'form': form})
    else:
        return render(request, 'profile/profile_king.html', { 'user_animal':user_animal, 'form': form})


def add_photo(request):
    if request.method == 'POST':
        form = edit_photo_form(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            user_animal = User_animal.objects.get(user=user.id)
            user_animal.photo = form.cleaned_data['photo']
            user_animal.save()
            return redirect('profile')
    else:
        form = edit_photo_form()
    return render(request, 'profile/profile_king.html', {'form':form})

def edit_profile(request):
    user = request.user
    usuario = User_animal.objects.get(user=user.id)

    dados = {
        'name': user.first_name,
        'last_name': user.last_name,
        'rg': usuario.rg,
        'cpf': usuario.cpf,
        'email': usuario.user.email,
        'telephone': usuario.telephone,
        'street': usuario.address.street,
        'number': usuario.address.number,
        'city': usuario.address.city,
        'neighborhood': usuario.address.neighborhood,
        'df': usuario.address.df,
        'status': 'edite'

    }
    form = usuario_form(initial = dados)
    return render(request, 'signup/signup.html', {'form': form})