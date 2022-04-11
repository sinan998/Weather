import requests
import json

while True:
    sehir=input("Lütfen hava durumunu öğrenmek istediğiniz şehrin adını giriniz: ")
    apiCode="API_KEY"
    adress="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&lang=tr&units=metric".format(sehir,apiCode)
    baglan=requests.get(adress)
    sorgu=baglan.json()
    havadurumu=sorgu["weather"][0]["description"]
    havasıcaklıgı=sorgu["main"]["temp"]
    hissedilensıcaklık=sorgu["main"]["feels_like"]
    minsıcaklık=sorgu["main"]["temp_min"]
    maxsıcaklık=sorgu["main"]["temp_max"]
    basınc=sorgu["main"]["pressure"]
    nem=sorgu["main"]["humidity"]
    konum=sorgu["name"]
    
    print("{} için hava durumu bilgileri Aşağıdaki gibidir\n\nSıcaklık: {}°\nDurum: {}\nHissedilen sıcaklık: {}°\nEn düşük sıcaklık: {}°\nEn yüksek sıcaklık: {}°\nBasınç: {} hpa\nNem: {} %".format(konum,havasıcaklıgı,havadurumu.title(),hissedilensıcaklık,minsıcaklık,maxsıcaklık,basınc,nem))