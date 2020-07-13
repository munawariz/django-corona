from django.shortcuts import render
import requests

def index(request):
    image = requests.get('https://covid19.mathdro.id/api/og')
    context = {
        'page_title': 'index',
        'image': image.url,
    }
    return render(request, 'index.html', context)

def global_case(request):
    data = requests.get('https://covid19.mathdro.id/api/').json()
    context = {
        'page_title': 'Global Case',
        'positif': data['confirmed']['value'],
        'sembuh': data['recovered']['value'],
        'meninggal': data['deaths']['value'],
    }
    return render(request, 'case.html', context)

def list_country(request):
    data = requests.get('https://covid19.mathdro.id/api/countries/').json()   
    data = data['countries']
    country_list = []
    link = []
    views_data = []
    
    for data in data:
        country_list.append(data['name'].lower())
        if ' ' in data['name']:
            link_name = data['name'].replace(' ', '')
            link.append(link_name.lower())
        else:
            link_name = data['name']
            link.append(data['name'].lower())
        views_data.append({'name':data['name'].lower(), 'link':link_name.lower()})
        
    context = {
        'page_title' : 'List Country',
        'country_list' : country_list,
        'links' : link,
        'data' : views_data,
    }
    return render(request, 'country_list.html', context)

def country(request, country_requested):
    if '%20' in country_requested:
        country_requested.replace('%20', ' ')
    data = requests.get(f'https://covid19.mathdro.id/api/countries/{country_requested}').json()
    print(data)

    # for data in data:
        # country = data['attributes']['Country_Region']
        # if country_requested.lower() in country.lower():
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
            # break
        # else:
        #     context = {
        #         'page_title' : 'Country Case',
        #         'country' : country_requested,
        #     }
    return render(request, 'case.html', context)
