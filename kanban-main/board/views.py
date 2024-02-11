from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.utils.formats import localize
from .forms import NewUserForm
from drf_yasg.utils import swagger_auto_schema


from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import APIView, api_view, permission_classes
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from rest_framework import generics, mixins, status
from drf_yasg import openapi


SWAGGER_SETTINGS = {
    "SUPPORTED_SUBMIT_METHOD": ['get', 'post', 'put', 'delete', ],
    'USE_SESSION_AUTH': False,
    "LOGIN_URL": "/",
    "LOGOUT_URL": "/",
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'description': 'Personal API Key authorization',
            'name': 'Authorization',
            'in': 'header',
        }
    },
    'APIS_SORTER': 'alpha',
    "SHOW_REQUEST_HEADERS": True,
    "VALIDATOR_URL": None,
    'api_key': 'veristoken fbe16f3a4c292c774c54', # An API key
}

@login_required

def home(request):
    all_tasks = []
    t_list = request.user.tasks.all()
    for t in t_list:
        t_dict = {
            'uuid': str(t.uuid),
            'name': t.name if t.name is not None else 'Без названия',
            'boardName': t.boardName,
            'date': str(localize(t.date))
        }
        all_tasks.append(t_dict)
    return render(request, 'index.html', {'tasks': all_tasks})


# @api_view(['POST'])
# @permission_classes([AllowAny,])


def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,
                             'Аккаунт зарегистрирован: '
                             'добро пожаловать на сайт!')
            return redirect('board:login')
        messages.error(request, 'Не удалось зарегистрировать аккаунт. '
                                'Проверьте корректность данных и '
                                'попробуйте еще раз!')
    form = NewUserForm()

    return render(request=request,
                  template_name='register.html',
                  context={'register_form': form})


# @api_view(['POST'])

@api_view(['POST','GET'])
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request,
                              f'Вы вошли на сайт под ником {username}.')
                return redirect('board:home')
            else:
                messages.error(request, 'Неверные имя и/или пароль.')
        else:
            messages.error(request, 'Неверные имя и/или пароль.')
    form = AuthenticationForm()
    return render(request=request, template_name='login.html',
                  context={'login_form': form})



@login_required
@api_view(['POST','GET'])
def logout_request(request):
    logout(request)
    messages.info(request, 'Вы вышли из аккаунта.')
    return redirect('board:login')
    # return Response(redirect('board:login'), status=status.HTTP_200_OK)

@login_required
@api_view(['POST','GET'])
def myuser(request):
    # logout(request)
    return redirect(request)

# from django.contrib.auth import logout
#
#
# def logout_view(request):
#     logout(request)
#     # Redirect to a success page.