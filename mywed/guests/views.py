from django.views.generic import FormView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from guests.forms import LoginForm


class LoginFormView(FormView):

    """ View for login guests """

    template_name = 'login.html'
    form_class = LoginForm
    success_url = 'index'


    def form_valid(self, form):
        login(self.request, form.user)
        return redirect(self.success_url)
