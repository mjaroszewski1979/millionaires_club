import os
import pandas_datareader.data as web
import numpy as np
from threading import Thread

cpi = []

def get_cpi_all(ticker):
    f = web.DataReader(ticker, 'econdb')
    f = f.values
    if np.mean(f[-12:]) < f[-1]:
        return 'ABOVE ITS 12-MONTH AVERAGE INDICATING INFLATION'
    else:
        return 'BELOW ITS 12-MONTH AVERAGE INDICATING DEFLATION'


data = {
    'UNITED STATES' : 'ticker=CPIUS',
    'CHINA' : 'ticker=CPICN',
    'JAPAN' : 'ticker=CPIJP',
    'GERMANY' : 'ticker=CPIDE',
    'FRANCE' : 'ticker=CPIFR',
    'INDIA' : 'ticker=CPIIN',
    'ITALY' : 'ticker=CPIIT',
    'BRAZIL' : 'ticker=CPIBR', 
    'SOUTH KOREA' : 'ticker=CPIKR',
    'CANADA' : 'ticker=CPICA',
    'RUSSIAN FEDERATION' : 'ticker=CPIRU',
    'SPAIN' : 'ticker=CPIES',
    'MEXICO' : 'ticker=CPIMX',
    'INDONESIA' : 'ticker=CPIID',
    'NETHERLANDS' : 'ticker=CPINL',
    'SAUDI ARABIA' : 'ticker=CPISA',
    'TURKEY' : 'ticker=CPITR',
    'SWITZERLAND' : 'ticker=CPICH',
    'TAIWAN' : 'ticker=CPITW',
    'POLAND' : 'ticker=CPIPL',
    'SWEDEN' : 'ticker=CPISE',
    'BELGIUM' : 'ticker=CPIBE',
    'ARGENTINA' : 'ticker=CPIAR',
    'THAILAND' : 'ticker=CPITH',
    'AUSTRIA' : 'ticker=CPIAT',
    'IRAN' : 'ticker=CPIIR',
    'NORWAY' : 'ticker=CPINO',
    'UNITED ARAB EMIRATES' : 'ticker=CPIAE',
    'NIGERIA' : 'ticker=CPING',
    'IRELAND' : 'ticker=CPIIE',
    'ISRAEL' : 'ticker=CPIIL',
    'SOUTH AFRICA' : 'ticker=CPIZA',
    'SINGAPORE' : 'ticker=CPISG',
    'HONG KONG' : 'ticker=CPIHK',
    'MALAYSIA' : 'ticker=CPIMY',
    'DENMARK' : 'ticker=CPIDK',
    'COLOMBIA' : 'ticker=CPICO',
    'PHILIPPINES' : 'ticker=CPIPH',
    'PAKISTAN' : 'ticker=CPIPK',
    'CHILE' : 'ticker=CPICL',
    'BANGLADESH' : 'ticker=CPIBD',
    'FINLAND' : 'ticker=CPIFI',
    'EGYPT' : 'ticker=CPIEG',
    'CZECH REPUBLIC' : 'ticker=CPICZ',
    'VIETNAM' : 'ticker=CPIVN',
    'PORTUGAL' : 'ticker=CPIPT',
    'ROMANIA' : 'ticker=CPIRO',
    'PERU' : 'ticker=CPIPE',
    'IRAQ' : 'ticker=CPIIQ',
    'GREECE' : 'ticker=CPIGR',
    'QATAR' : 'ticker=CPIQA',
    'ALGERIA' : 'ticker=CPIDZ',
    'KAZAKHSTAN' : 'ticker=CPIKZ',
    'HUNGARY' : 'ticker=CPIHU',
    'KUWAIT' : 'ticker=CPIKW',
    'UKRAINE' : 'ticker=CPIUA',
    'MOROCCO' : 'ticker=CPIMA',
    'ECUADOR' : 'ticker=CPIEC',
    'SLOVAKIA' : 'ticker=CPISK',
    'ANGOLA' : 'ticker=CPIAO',
    'VENEZUELA' : 'ticker=CPIVE',
    'SRI LANKA' : 'ticker=CPILK',
    'KENYA' : 'ticker=CPIKE',
    'DOMINICAN REPUBLIC' : 'ticker=CPIDO',
    'ETHIOPIA' : 'ticker=CPIET',
    'OMAN' : 'ticker=CPIOM',
    'GUATEMALA' : 'ticker=CPIGT',
    'LUXEMBOURG' : 'ticker=CPILU',
    'MYANMAR' : 'ticker=CPIMM',
    'GHANA' : 'ticker=CPIGH',
    'BULGARIA' : 'ticker=CPIBG',
    'PANAMA' : 'ticker=CPIPA',
    'CROATIA' : 'ticker=CPIHR',
    'URUGUAY' : 'ticker=CPIUY',
    'BELARUS' : 'ticker=CPIBY',
    'TANZANIA' : 'ticker=CPITZ',
    'LEBANON' : 'ticker=CPILB',
    'MACAO' : 'ticker=CPIMO',
    'SLOVENIA' : 'ticker=CPISI',
    'LITHUANIA' : 'ticker=CPILT',
    'UNITED KINGDOM' : 'ticker=CPIUK'
}
def get_cpi(symbol):
    global cpi
    countries  = {
            'ticker=CPICN' : 'CHINA',
            'ticker=CPIDE' : 'GERMANY',
            'ticker=CPIIN' : 'INDIA',
            'ticker=CPIJP' : 'JAPAN',
            'ticker=CPIUS' : 'UNITED STATES'
        }
    f = web.DataReader(symbol, 'econdb').values
    if np.mean(f[-12:]) < f[-1]:
        result = ['INFLATION', countries[symbol]]
    else:
        result = ['DEFLATION', countries[symbol]]
    if result not in cpi:
        cpi.append(result)
        cpi.sort(key=lambda x: x[1])

    
def get_cpi_g5():
    global cpi

    threads = []
    num_threads = 5
    tickers = ['ticker=CPICN', 'ticker=CPIDE', 'ticker=CPIIN', 'ticker=CPIJP', 'ticker=CPIUS']

    for i in range(num_threads):
        for x in tickers:
            thread = Thread(target=get_cpi, args=(x,))
            threads.append(thread)

    for thread in threads:
        thread.start()

    return cpi



