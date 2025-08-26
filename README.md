# automated-hydroponics 🌱
> Uzaktan İzleme ile Otomatik Hidroponik Sistem

<p>
  <a href="https://github.com/wadzee/automated-hydroponics/blob/master/LICENSE">
    <img alt="Lisans: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" target="_blank" />
  </a>
</p>

**Kısa açıklama** :

  > Bu proje hidroponik teknik kullanarak iç mekanda bitki yetiştirmeye odaklanır.
  > Bu nedenle geliştirilen çoğu özellik/gereksinim bu tekniğe yöneliktir.
  > Sistem şu anda mevcut pH, EC ve ortam ışığını izleyebilmektedir.
  > Şimdilik bitirme projem olduğundan bazı ek kodları yükleyemiyorum. Hazır olduğunda tüm içeriği paylaşacağım. Teşekkürler.

# Özellikler!

  - Sistem ile yetiştirilecek bitki türünü belirtme (Marul, Kale vb.)
  - Otomatik pH ve EC Dozlama Mekanizması
  - Kullanıcı dostu web arayüzünde anlık bitki durumu izleme
  - Ortam ışığına göre ışık kaynağını otomatik Aç/Kapat

![p](features.PNG)

Web sitesinden görüntülendiğinde

![p](monitor.PNG)

**Önemli Not**:
  - FYP (Final Year Project) kapsamında devam eden bir proje olduğu için bazı kod/özellikler depoda eksiktir.

# Demo

LDR sensörü siyah bir kutu ile kapatıldığında LDR değeri **Gerçek Zamanlı** olarak güncellenir. (diğer sensörlerde de çalışır)

![p](ldrdemo.gif)

## Donanım Gereksinimleri

Bu projede aşağıdaki donanımlar kullanılmıştır, uyumlu ise kendi donanımlarınızı da kullanabilirsiniz.

| Donanım | Bağlantılar |
| ------ | ------ |
| Arduino Uno R3 | [Amazon](https://www.amazon.com/Arduino-A000066-ARDUINO-UNO-R3/dp/B008GRTSV6) |
| Raspberry Pi 3B+ | [Amazon](https://www.amazon.com/ELEMENT-Element14-Raspberry-Pi-Motherboard/dp/B07BDR5PDW/ref=sr_1_3?crid=2MHYPOB2GXUSW&keywords=raspberry+pi+3+b%2B&qid=1561152106&s=electronics&sprefix=raspberry+pi+3%2Celectronics%2C456&sr=1-3) |
| PH Sensörü | [AliExpress](https://www.aliexpress.com/item/32805675619.html?spm=a2g0s.9042311.0.0.468f4c4dS0tnBH) |
| EC Sensörü | [DIY](https://hackaday.io/project/7008-fly-wars-a-hackers-solution-to-world-hunger/log/24646-three-dollar-ec-ppm-meter-arduino) |
| LDR | [Amazon](https://www.amazon.com/10pcs-Dependent-Resistor-Photoresistor-GL5528/dp/B00XDT8KI4) |
| Röle | [Amazon](https://www.amazon.com/JBtek-Channel-Module-Arduino-Raspberry/dp/B00KTEN3TM/ref=sr_1_3?keywords=4+channel+relay&qid=1561157309&s=gateway&sr=8-3) |
| Pompa | [Amazon](https://www.amazon.com/Gikfun-Submersible-Fountain-Aquarium-EK1893/dp/B07BHD6KXS/ref=pd_lpo_sbs_60_t_0?_encoding=UTF8&psc=1&refRID=TQYTT601T1NQPXQKMPNE) |

## Fritzing Çizimleri

Donanım bağlantıları için çizim. Fritzing dosyasını [buradan](https://github.com/wadzee/automated-hydroponics/blob/master/Fritzing%20Sketches.fzz) edinebilirsiniz.

![p](Sketches.png)

## Ön Koşullar

Raspbian çalıştıran Raspberry Pi 3 gereklidir.

[Node-RED](https://nodered.org/) gerektirir

[Arduino IDE](https://www.arduino.cc/) gerektirir

Arduino Uno, USB bağlantısı ile Raspberry Pi'ye bağlanmalıdır.

![p](how%20to%20connect.PNG)

## Kurulum

### Node-RED
Node-RED'i kurmak için Terminal açıp aşağıdaki komutu çalıştırın

```sh
bash <(curl -sL https://raw.githubusercontent.com/node-red/raspbian-deb-package/master/resources/update-nodejs-and-nodered)
```

### Arduino IDE
Arduino IDE'yi kurmak için Terminal açıp aşağıdaki komutları çalıştırın

```sh
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install arduino
```

## Çalıştırma

Node-RED'i başlatmak için Terminal'de aşağıdaki komutu çalıştırın

```sh
node-red-start
```

Varsayılan sunucu adresine tarayıcınızla giderek Node-RED'in çalıştığını doğrulayın

```sh
127.0.0.1:1880
```

Bu [dosyayı](https://github.com/wadzee/automated-hydroponics/blob/master/flows.json) Node-RED panosuna içe aktarın.

**Not**
- USB portunu Arduino'nuzun bağlı olduğu doğru porta değiştirin.
- Çakışmayı önlemek için `Sensor Data` dosya adresini kendi adresinizle değiştirin.
***

## Yazar

👤 **Radzi Ramli**

* GitHub: [@wadzee](https://github.com/wadzee)

## Destek Olun

Bu proje size yardımcı olduysa bir ⭐️ verin!

## 📝 Lisans

Telif Hakkı © 2019 [Radzi Ramli](https://github.com/wadzee).<br />
Bu proje [MIT](https://github.com/wadzee/automated-hydroponics/blob/master/LICENSE) lisanslıdır.

## Python Araçları ve API

Bu depo artık Arduino sensörlerinden seri verileri okuyup bir API'ye göndermek için `sensor_monitor.py` betiğini içeriyor. Buna eşlik eden `api_server.py` dosyası, okumaları bellekte saklamak için basit bir REST arayüzü sağlar.

### API Sunucusunu Çalıştırma

```sh
pip install flask
python api_server.py
```

### Mobil Web Arayüzü

`mobile/` dizini, en son sensör değerlerini getiren temel bir mobil uyumlu sayfa içerir. API sunucusunu çalıştırın ve tarayıcınızda `mobile/index.html` dosyasını açın.

