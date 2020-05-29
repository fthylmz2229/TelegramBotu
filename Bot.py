#kullanılan kütüphaneler
import requests

import DovizKurlari
import corona
import meyvesebze

#API bağlantısı için gerekli olan parametreler
token = "--TELEGRAM API TOKEN IS HERE--"
chat_id = "1051278240"
#mesajlaşma esnasında verilecek cevapları belirlemek için gelen mesajı tespit etmek için kullanılan değişkenler
gelenYazi = ""
oncekiGelenYazi = ""
gonderilecekYazi = "Merhaba biraz sohbet edelimmi?"
oncekiGonderilecekYazi = ""
simdikiLen = 0
oncekiLen = 0
# uygulama sürekli olarak son mesajı okuyarak yeni gelen mesaj varmı diye kontrol ediyor
while True:
    try:
        #mesajları okuyoruz
        reqGet = requests.get(url="https://api.telegram.org/bot{0}/getupdates?offset=672581323".format(token))
        #gelen cevaptan kaç mesaj olduğunu okuyoruz.
        lenResult = len(reqGet.json()["result"])
        #fark var ise yeni mesaj gelmiş demektir
        if lenResult != oncekiLen:
            # önceki mesaj sayısı ile yeni mesaj sayısı farklı ise yeni mesaj var demektir.
            oncekiLen = simdikiLen
            simdikiLen = lenResult
            #gelen mesaj var ise
            if lenResult > 0:
                if oncekiLen != simdikiLen:
                    gelenYazi = reqGet.json()["result"][lenResult-1]["message"]["text"]
                    if lenResult > 1:
                        oncekiGelenYazi = reqGet.json()["result"][lenResult-2]["message"]["text"]
                    #lokal veritabanları için dosya okuma ve yazma ilemlerimizi tanımlıyoruz
                    readFile = open("venv/bilgibankasi.txt", "r")
                    writeFile = open("venv/bilgibankasi.txt", "rt")
                    yasakKelimeler = open("venv/yasakkelimeler.txt", "r")
                    # kaydedilmesi gereken veri geldi.
                    if oncekiGonderilecekYazi == "Adını bilmiyorum söylersen aklımda tutabilirim ve sana daha sonra bu isimle hitap edebilirim.":
                        data = writeFile.read()
                        data = data.replace('isim:;', 'isim:' + gelenYazi + ';')
                        writeFile.close()
                        writeFile = open("venv/bilgibankasi.txt", "wt")
                        writeFile.write(data)
                        writeFile.close()
                        gonderilecekYazi = "Adını aklımda tutacağım " + gelenYazi + ". Teşekkürler."

                        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': chat_id, 'text': gonderilecekYazi}).json()
                        oncekiGelenYazi = gelenYazi
                        oncekiGonderilecekYazi = gonderilecekYazi
                    elif oncekiGonderilecekYazi == "Soyadını bilmiyorum söylersen aklımda tutabilirim.":
                        data = writeFile.read()
                        data = data.replace('soyad:;', 'soyad:' + gelenYazi + ';')
                        writeFile.close()
                        writeFile = open("venv/bilgibankasi.txt", "wt")
                        writeFile.write(data)
                        writeFile.close()
                        gonderilecekYazi = "Soyadını aklımda tutacağım. Teşekkürler."

                        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': chat_id, 'text': gonderilecekYazi}).json()
                        oncekiGelenYazi = gelenYazi
                        oncekiGonderilecekYazi = gonderilecekYazi
                    elif oncekiGonderilecekYazi == "Tuttuğun takımı bilmiyorum söylersen aklımda tutabilirim.":
                        data = writeFile.read()
                        data = data.replace('takim:;', 'takim:' + gelenYazi + ';')
                        writeFile.close()
                        writeFile = open("venv/bilgibankasi.txt", "wt")
                        writeFile.write(data)
                        writeFile.close()
                        gonderilecekYazi = "Tuttuğun takımı aklımda tutacağım. Teşekkürler."

                        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': chat_id, 'text': gonderilecekYazi}).json()
                        oncekiGelenYazi = gelenYazi
                        oncekiGonderilecekYazi = gonderilecekYazi
                    elif oncekiGonderilecekYazi == "Yaşını bilmiyorum söylersen aklımda tutabilirim.":
                        data = writeFile.read()
                        data = data.replace('yas:;', 'yas:' + gelenYazi + ';')
                        writeFile.close()
                        writeFile = open("venv/bilgibankasi.txt", "wt")
                        writeFile.write(data)
                        writeFile.close()
                        gonderilecekYazi = "Yaşını aklımda tutacağım. Teşekkürler."

                        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': chat_id, 'text': gonderilecekYazi}).json()
                        oncekiGelenYazi = gelenYazi
                        oncekiGonderilecekYazi = gonderilecekYazi
                    else:
                        # cevaplanması gereken soru geldi.
                        if gelenYazi != oncekiGelenYazi:
                            if gonderilecekYazi != "Merhaba biraz sohbet edelimmi?":
                                yasakKelimelerData = yasakKelimeler.readlines()
                                if gelenYazi.lower() in str(yasakKelimelerData).lower():
                                    gonderilecekYazi = "Aaa. Çok ayıp!"
                                elif "adın" in gelenYazi.lower():
                                    gonderilecekYazi = "Ben bir robotum. Bana robotum diye hitap edebilirsin."
                                elif "yaşın" in gelenYazi.lower():
                                    gonderilecekYazi = "09.03.2020 tarihinde senin tarafından yaratıldım."
                                elif "patates" in gelenYazi.lower():
                                    patates = meyvesebze.MeyveSebze()
                                    deger = patates.FiyatGetir("patates")
                                    gonderilecekYazi = "Patatesin Fiyatı: " + deger
                                elif "soğan" in gelenYazi.lower() or "sogan" in gelenYazi.lower():
                                    sogan = meyvesebze.MeyveSebze()
                                    deger = sogan.FiyatGetir("soğan")
                                    gonderilecekYazi = "Soğanın Fiyatı: " + deger
                                elif "corona" in gelenYazi.lower():
                                    vaka = corona.Corona()
                                    deger = vaka.GetirTurkiye()
                                    gonderilecekYazi = "Türkiyedeki Güncel Veriler\n--------------------------------------\n" + deger
                                elif "dolar" in gelenYazi.lower():
                                    kur = DovizKurlari.DovizKurlari()
                                    deger = kur.DegerSor("USD",4)
                                    gonderilecekYazi = "Dolar: " + deger + " TL."
                                elif "euro" in gelenYazi.lower():
                                    kur = DovizKurlari.DovizKurlari()
                                    deger = kur.DegerSor("EUR",4)
                                    gonderilecekYazi = "Euro: " + deger + " TL."
                                elif "soyadım" in gelenYazi.lower():
                                    lines = readFile.readlines()
                                    soyad = lines[1]
                                    if "soyad:;" not in soyad:
                                        gonderilecekYazi = soyad[6:len(soyad)-2]
                                    else:
                                        gonderilecekYazi = "Soyadını bilmiyorum söylersen aklımda tutabilirim."
                                    readFile.close()
                                elif "adım" in gelenYazi.lower():
                                    lines = readFile.readlines()
                                    ad = lines[0]
                                    if "isim:;" not in ad:
                                        gonderilecekYazi = ad[5:len(ad)-2]
                                    else:
                                        gonderilecekYazi = "Adını bilmiyorum söylersen aklımda tutabilirim ve sana daha sonra bu isimle hitap edebilirim."
                                    readFile.close()
                                elif "takım" in gelenYazi.lower():
                                    lines = readFile.readlines()
                                    takim = lines[2]
                                    if "takim:;" not in takim:
                                        gonderilecekYazi = takim[6:len(takim)-2]
                                    else:
                                        gonderilecekYazi = "Tuttuğun takımı bilmiyorum söylersen aklımda tutabilirim."
                                    readFile.close()
                                elif "yaş" in gelenYazi.lower():
                                    lines = readFile.readlines()
                                    yas = lines[3]
                                    if "yas:;" not in yas:
                                        gonderilecekYazi = yas[4:len(yas)-2]
                                    else:
                                        gonderilecekYazi = "Yaşını bilmiyorum söylersen aklımda tutabilirim."
                                    readFile.close()
                                elif "nasılsın" in gelenYazi.lower():
                                    lines = readFile.readlines()
                                    isim = lines[0]
                                    if len(isim) > 6:
                                        gonderilecekYazi = "İyiyim sen nasılsın " + ad[5:len(isim)-2] + "."
                                    else:
                                        gonderilecekYazi = "İyiyim sen nasılsın."
                                elif "merhaba" in gelenYazi.lower():
                                    lines = readFile.readlines()
                                    isim = lines[0]
                                    if len(isim) > 6:
                                        gonderilecekYazi = "Merhaba " + ad[5:len(isim)-2] + "."
                                    else:
                                        gonderilecekYazi = "Merhaba."
                                elif "benimle evlenirmisin" in gelenYazi.lower():
                                    gonderilecekYazi = "Kullanıcı lisans sözleşmesine göre evlenemeyiz."
                                else:
                                    gonderilecekYazi = "Buna nasıl cevap vereceğimi bilmiyorum."
                            # yukarıdaki algoritma vasıtasıyla elde ettiğimiz dönüş değerini telegram API vasıtasıyla kullanıcıya iletiyoruz.
                            requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': chat_id, 'text': gonderilecekYazi}).json()
                            # daha sonra yeni mesajlar için sıfırlama işlemini gerçekleştiriyoruz
                            oncekiGelenYazi = gelenYazi
                            oncekiGonderilecekYazi = gonderilecekYazi
                            gonderilecekYazi = ""
    except:
        print("hata")
        gonderilecekYazi = "Hata oluştu!"
        # yhata mesajını telegram API vasıtasıyla kullanıcıya iletiyoruz.
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': chat_id, 'text': gonderilecekYazi}).json()
        #daha sonra yeni mesajlar için sıfırlama işlemini gerçekleştiriyoruz
        oncekiGelenYazi = gelenYazi
        oncekiGonderilecekYazi = gonderilecekYazi
        gonderilecekYazi = ""