from django.shortcuts import render
import requests

def index(request):
    context = {
        'page_title': 'index',
    }
    return render(request, 'index.html', context)

def global_case(request):
    positif = requests.get('https://api.kawalcorona.com/positif').json()
    sembuh = requests.get('https://api.kawalcorona.com/sembuh').json()
    meninggal = requests.get('https://api.kawalcorona.com/meninggal').json()
    context = {
        'page_title': 'Global Case',
        'positif': positif['value'],
        'sembuh': sembuh['value'],
        'meninggal': meninggal['value'],
    }
    return render(request, 'index.html', context)

def list_country(request):
    data = requests.get('https://api.kawalcorona.com/').json()
    country_list = []
    for data in data:
        country = data['attributes']['Country_Region']
        country_list.append(country)
    context = {
        'page_title' : 'List Country',
        'country_list' : country_list,
    }
    return render(request, 'index.html', context)

def country(request, country_requested):
    data = requests.get('https://api.kawalcorona.com/').json()

    for data in data:
        country = data['attributes']['Country_Region']
        if country_requested.lower() in country.lower():
            positif = data['attributes']['Confirmed']
            sembuh = data['attributes']['Recovered']
            meninggal = data['attributes']['Deaths']
            context = {
                'page_title' : 'Country Case',
                'country' : country_requested,
                'positif': positif,
                'sembuh': sembuh,
                'meninggal': meninggal,
            }
            break
        else:
            context = {
                'page_title' : 'Country Case',
                'country' : country_requested,
            }
    return render(request, 'index.html', context)
