from django.shortcuts import render
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect('/?account=success')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
class LoginLogout(LoginView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'message': 'You have logged out!',
            'tag': 'success'
        })
        return context
def logout_view(request):
    logout(request)
    return LoginLogout.as_view(template_name='users/login.html')(request)
