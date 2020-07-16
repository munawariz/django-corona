from django.shortcuts import render
from asgiref.sync import sync_to_async
import requests
import asyncio



def index(request):
    data = requests.get('https://covid19.mathdro.id/api/').json()
    image = requests.get('https://covid19.mathdro.id/api/og')
    context = {
        'country': 'Global',
        'positif': data['confirmed']['value'],
        'sembuh': data['recovered']['value'],
        'meninggal': data['deaths']['value'],
        'last_update': data['lastUpdate'],
        'gambar': image.url,
    }
    return render(request, 'page/case.html', context)

def list_country(request):
    data = requests.get('https://covid19.mathdro.id/api/countries/').json()   
    data = data['countries']
    country_list1 = []
    country_list2 = []
    country_list3 = []
    pointer = 0    
    
    for data in data:
        if pointer % 3 == 0:
            country_list1.append(data['name'].lower())
        elif pointer % 3 == 1:
            country_list2.append(data['name'].lower())
        elif pointer % 3 == 2:
            country_list3.append(data['name'].lower())
        pointer += 1
        
    context = {
        'country_list1' : country_list1,
        'country_list2' : country_list2,
        'country_list3' : country_list3,
    }
    return render(request, 'page/countries.html', context)

def country(request, *, country_requested):
    data = requests.get(f'https://covid19.mathdro.id/api/countries/{country_requested}').json()
    image = requests.get(f'https://covid19.mathdro.id/api/countries/{country_requested}/og')

    positif = data['confirmed']['value']
    sembuh = data['recovered']['value']
    meninggal = data['deaths']['value']
    last_update = data['lastUpdate']
    context = {
        'country' : country_requested,
        'positif': positif,
        'sembuh': sembuh,
        'meninggal': meninggal,
        'last_update': last_update,
        'gambar': image.url,
    }
 
    return render(request, 'page/case.html', context)