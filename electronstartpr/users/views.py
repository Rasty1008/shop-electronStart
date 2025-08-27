from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import auth, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm, UserForgotpasswordForm, UserSetPasswordForm


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = UserLoginForm

    def get_success_url(self):
        redirect_page = self.request.POST.get('next', None)
        if redirect_page and redirect_page != reverse('users:logout'):
            return redirect_page
        return reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context


class UserRegistrationView(CreateView):
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        messages.success(self.request, 'Вы успешно зарегистрированы и вошли в систему.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context
    

class UserProfileView(LoginRequiredMixin,UpdateView):
    template_name = 'users/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Профиль успешно обновлен.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при обновлении профиля. Пожалуйста, исправьте ошибки.')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Личный кабинет'
        return context


class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    '''Сброс пароля по почте'''

    form_class = UserForgotpasswordForm
    template_name = 'users/password_reset.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Инструкции по восстановлению пароля отправлены на ваш email.'
    subject_template_name = 'users/password_subject_reset_mail.txt'
    email_template_name = 'users/password_reset_mail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Восстановление пароля'
        return context
    
class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    '''Установка нового пароля'''
    
    form_class = UserSetPasswordForm
    template_name = 'users/password_reset_new.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Ваш пароль успешно изменен.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Установка нового пароля'
        return context



@login_required
def logout(request):
    messages.success(request, 'Вы успешно вышли из системы.')
    auth.logout(request)
    return redirect(reverse('main:index'))



# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 messages.success(request, 'Вы успешно вошли в систему.')

#                 if request.POST.get('next', None):
#                     return HttpResponseRedirect(request.POST.get('next'))
                
#                 return HttpResponseRedirect(reverse('main:index'))
#     else:
#         form = UserLoginForm()

#     context = {
#         'title': 'Авторизация',
#         'form': form
        
#     }
#     return render(request, 'users/login.html', context)

# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.instance
#             auth.login(request, user)
#             messages.success(request, 'Вы успешно зарегистрированы и вошли в систему.')
#             return HttpResponseRedirect(reverse('main:index'))
#     else:
#         form = UserRegistrationForm()

#     context = {
#         'title': 'Регистрация',
#         'form': form
#     }
#     return render(request, 'users/registration.html', context)

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(instance=request.user, data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Профиль успешно обновлен.')
#             return HttpResponseRedirect(reverse('users:profile'))
#     else:
#         form = ProfileForm(instance=request.user)

#     context = {
#         'title': 'Личный кабинет',
#         'form': form
#     }
#     return render(request, 'users/profile.html', context)

