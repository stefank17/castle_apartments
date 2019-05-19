
from django.shortcuts import render, redirect, get_object_or_404
from users.models import Profile, ViewingHistory
from apartments.models import Apartment

from users.forms.register_form import UserCreationForm
from users.forms.user_form import ProfileForm, UserForm

from django.contrib.auth.models import User

# register function is checked
def register(request):
    # return render(request, 'users/register.html')
    if request.method == 'POST':
        # TODO: Create UserCreateForm()
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'users/register.html', {
        'form': UserCreationForm()
    })

# Sækir notanda eftir ID og finnur profile hans
def get_user_by_id(request, id):
    apartments_viewed = ViewingHistory.objects.filter(user_id=id).order_by('-time')
    user_history = []
    for apartment in apartments_viewed:
        user_history.append(get_object_or_404(Apartment, pk=apartment.apartment_id))
    apartments_owned = Apartment.objects.filter(owner_id = id)
    return render(request, 'users/profile.html', {
        'userprofile': get_object_or_404(User, pk=id),
        'user_history': user_history,
        'apartments_owned': apartments_owned
    })

# Skilar profile síðu
def profile(request):
    return render(request, 'users/profile.html')

# Finnur notanda og býr til form til að uppfæra gögn hjá notandanum
def edit_profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    user = User.objects.filter(pk = request.user.pk).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        userform = UserForm(instance=user, data=request.POST)
        if form.is_valid():
            if userform.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                user.save()

        return redirect('edit_profile')
    return render(request, 'users/edit_profile.html', {
        'profileform': ProfileForm(instance=profile),
        'userform': UserForm(instance=user),
    })
