from django.shortcuts import render
from .models import HomeLogo, HomeInfo, HomeSlider, HomeFooterBg, LastEpisode
# Create your views here.

def double_content():
    homelogo = HomeLogo.objects.all()[0]
    homefooterbg = HomeFooterBg.objects.all()[0]
    return [homelogo, homefooterbg]


def index(request):
    hominfo = HomeInfo.objects.all()[0]
    home_slider = HomeSlider.objects.all()
    last_episode = HomeSlider.objects.all()
    return render(request, 'main/index.html', context={
        'act':'index',
        'homelogo':double_content()[0],
        'hominfo':hominfo,
        'home_slider':home_slider,
        'homefooterbg':double_content()[1],
        'last_episode':last_episode
    })


def about(request):
    return render(request, 'main/about.html', context={
        'act':'about',
        'homelogo':double_content()[0]

    })


def contact(request):
    return render(request, 'main/contact.html', context={
        'act':'contact',
        'homelogo':double_content()[0]

    })


def detail_page(request):
    return render(request, 'main/detail-page.html', context={
        'act':'detail_page',
        'homelogo':double_content()[0]

    })


def listing_page(request):
    last_episode = HomeSlider.objects.all()
    return render(request, 'main/listing-page.html', context={
        'act':'listing_page',
        'homelogo':double_content()[0],
        'last_episode':last_episode

    })