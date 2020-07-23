from django.shortcuts import render
from django.http import HttpResponseNotFound
import requests
from django.conf.urls import handler404
import pandas as pd
from datetime import datetime


def index(request):
    try:
        data = requests.get('https://corona-api.com/timeline').json()
        last_data = data['data'][0]
        prev_data = []

        for x in range(3):
            prev_data.append(data['data'][x+1])        

        context = {
            'data': last_data,
            'prev_data': prev_data,
        }
        return render(request, 'page/global.html', context)
    except Exception as e:
        print(e)

def list_country(request):
    try:
        data = requests.get('https://corona-api.com/countries').json()   
        data = data['data']
        country_list1 = []
        country_list2 = []
        country_list3 = []
        code_list1 = []
        code_list2 = []
        code_list3 = []
        pointer = 0    
        
        for data in data:
            if pointer % 3 == 0:            
                country_list1.append(data['name'].lower())
                code_list1.append(data['code'])
            elif pointer % 3 == 1:
                country_list2.append(data['name'].lower())
                code_list2.append(data['code'])
            elif pointer % 3 == 2:
                country_list3.append(data['name'].lower())       
                code_list3.append(data['code'])
            pointer += 1

        context = {
            'dict_list1' : dict(zip(code_list1, country_list1)),
            'dict_list2' : dict(zip(code_list2, country_list2)),
            'dict_list3' : dict(zip(code_list3, country_list3)),
        }
        return render(request, 'page/countries.html', context)
    except Exception as e:
        print(e)

def country(request, *, country_requested):
    try:
        data = requests.get(f'https://corona-api.com/countries/{country_requested}').json()
        last_data = data['data']
        prev_data = []        
        timeline_data = []
        
        try:
            for x in range(3):                       
                timeline = data['data']['timeline'][x+1]   
                if timeline:
                    # dates = datetime.strptime(timeline['date'] , '%Y-%m-%d')
                    # timeline_data.append([dates, int(timeline['confirmed']), int(timeline['recovered']), int(timeline['deaths'])])
                    timeline_data.append(['ok', 21, 22, 23])
                    prev_data.append(timeline)
        except IndexError:
            pass

        df = pd.DataFrame(timeline_data, columns=['Date', 'Confirmed', 'Recovered', 'Deaths'])
        df.plot(title=f'ok COVID-19 Case')
        
        context = {
            'data': last_data,
            'latest_date': last_data['updated_at'][0:10],
            'prev_data': prev_data,
        }
    
        return render(request, 'page/case.html', context)
    except Exception as e:
        print('the error is ',e)

def dev(request):
    return render(request, 'page/dev.html')

def error_404(request, exception):
    return render(request, 'page/error404.html')

def error_500(request):
    return render(request, 'page/error404.html')