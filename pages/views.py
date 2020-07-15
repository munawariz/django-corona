from django.shortcuts import render
import requests

def index(request):
    data = requests.get('https://covid19.mathdro.id/api/').json()
    context = {
        'positif': data['confirmed']['value'],
        'sembuh': data['recovered']['value'],
        'meninggal': data['deaths']['value'],
    }
    return render(request, 'page/index.html', context)

def list_country(request):
    data = requests.get('https://covid19.mathdro.id/api/countries/').json()   
    data = data['countries']
    country_list = []
    
    for data in data:
        country_list.append(data['name'].lower())
        
    context = {
        'country_list' : country_list,
    }
    return render(request, 'page/countries.html', context)

def country(request, *, country_requested):
    data = requests.get(f'https://covid19.mathdro.id/api/countries/{country_requested}').json()

    positif = data['confirmed']['value']
    sembuh = data['recovered']['value']
    meninggal = data['deaths']['value']
    context = {
        'page_title' : 'Country Case',
        'country' : country_requested,
        'positif': positif,
        'sembuh': sembuh,
        'meninggal': meninggal,
    }
 
    return render(request, 'case.html', context)
