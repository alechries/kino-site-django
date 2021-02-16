from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .. import models, forms as g_forms
import datetime


def index_view(request):
    now = datetime.date.today()
    full_date_now = datetime.date.today()
    background_banner = models.BackgroundBanner.get_solo()
    films_today = models.Film.objects.filter(first_night__lte=now)
    print(films_today)
    future_film = models.Film.objects.filter(first_night__gt=now)
    print(future_film)
    return render(request, 'public/index.html', {'background_banner': background_banner,
                                                 'films_today': films_today,
                                                 'future_film': future_film,
                                                 'date_now': full_date_now,
                                                 })


def account_cabinet_view(request):
    return render(request, 'public/account/cabinet.html')


def account_login_view(request):
    if request.method == 'POST':
        form = g_forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request,
                                username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('public_views.index')
                else:
                    _message = 'User is not active'
            else:
                _message = 'User does not exist'
        else:
            _message = 'Data is incorrect'
    else:
        _message = 'Please, Sign in'
    return render(request, 'public/account/login.html', {'form': g_forms.LoginForm(), 'message': _message})


def account_logout_view(request):
    logout(request)
    return redirect('index')


def account_registration_view(request):
    form = g_forms.RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        login(request, user)  # , backend='django.contrib.auth.backends.ModelBackend'
        form.save()
        return redirect('public_views.index')
    return render(request, 'public/account/registration.html', context={'form': g_forms.RegisterForm()})


def posters_films_list_view(request):
    return render(request, 'public/posters/films_list.html')


def posters_films_details_view(request, pk):
    film = models.Film.objects.filter(id=pk)
    background_banner = models.BackgroundBanner.get_solo()
    return render(request, 'public/posters/film_details.html', {'film': film,
                                                                'background_banner': background_banner,
                                                                })


def timetable_films_sessions_list_view(request):
    return render(request, 'public/timetable/films-sessions-list.html')


def timetable_reservation_view(request, pk):
    return render(request, 'public/timetable/reservation.html')


def cinema_list_view(request):
    return render(request, 'public/cinema/list.html')


def cinema_details_view(request, pk):
    return render(request, 'public/cinema/details.html')


def cinema_hall_details_view(request, pk):
    return render(request, 'public/cinema/hall_details.html')


def promotion_list_view(request):
    return render(request, 'public/promotion/list.html')


def promotion_details_view(request, pk):
    return render(request, 'public/promotion/details.html')


def about_cinema_view(request):
    return render(request, 'public/about/cinema.html')


def about_news_view(request):
    return render(request, 'public/about/news.html')


def about_cafe_bar_view(request):
    return render(request, 'public/about/cafe-bar.html')


def about_vip_hall_view(request):
    return render(request, 'public/about/vip-hall.html')


def about_advertising_view(request):
    return render(request, 'public/about/advertising.html')


def about_mobile_app_view(request):
    return render(request, 'public/about/mobile-app.html')


def about_child_room_view(request):
    return render(request, 'public/about/child-room.html')


def about_contacts_view(request):
    return render(request, 'public/about/contacts.html')