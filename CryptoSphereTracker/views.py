# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


from django.http import HttpResponse
from cryptos.models import CryptoBalance




# Create views here below:



# home page should
def home_page(request):
    import requests
    import json

    #crypto prices for ticker at top
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC,XRP,TRX&tsyms=USD")
    price = json.loads(price_request.content)


    pricesNdInfo_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,LTC,BCH,EOS,XLM,XMR,ADA,TRX&tsyms=USD")
    prices = json.loads(pricesNdInfo_request.content)

    return render(request, 'home.html', {'price':price, 'prices':prices})




def news_page(request):
    import requests
    import json
    # crypto news
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'news.html', {'api': api})




def portfolio_page(request):
    import requests
    import json


    userBalance = CryptoBalance.objects.all()


    #get prices and info
    #
    pricesPortfolio_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,LTC,BCH,EOS,XLM,XMR,ADA,TRX&tsyms=USD,BTC")
    pricesP = json.loads(pricesPortfolio_request.content)
    return render(request, 'portfolio.html', {'prices':pricesP, 'user':userBalance})



def show_page(request):
    import requests
    import json


    return render(request, 'show.html')
