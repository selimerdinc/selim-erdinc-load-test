<p align="center">
  <img src="https://locust.io/static/img/logo.png" alt="Locust Logo" width="200"/>
</p>

# 📈 N11 Arama Modülü Yük Testi

![Locust](https://img.shields.io/badge/Locust-Performance%20Testing-brightgreen)  
![Python](https://img.shields.io/badge/Python-3.6+-blue)

> **Locust** ile N11 Arama Modülü üzerinde yük testi gerçekleştiriyoruz.  
> Sanal kullanıcılar ile performans ölçümü ve hata takibi yaparak, sistemin dayanıklılığını analiz ediyoruz.

---

## 🚀 Kurulum

1. **Projeyi klonlayın:**

   ```bash
   git clone https://github.com/selimerdinc/selim-erdinc-load-test.git
   cd selim-erdinc-load-test
   ```

2. **Bağımlılıkları yükleyin:**

   ```bash
   pip install locust
   ```

3. **Locust ile testi başlatın:**

   ```bash
   locust -f main.py --users 100 --spawn-rate 10 --host https://www.n11.com
   ```

4. **Web arayüzünü kullanın:**

   - Tarayıcıdan `http://localhost:8089` adresine erişin.
   - Kullanıcı sayısını ve oluşturulma hızını ayarlayarak testi başlatın.

---

## 📋 Test Senaryosu

🔎 **Arama Çubuğu Testi**

- `/arama?q=bilgisayar` endpoint'ine istek gönderilir.
- Dönen yanıtta:
  - **HTTP 200** durumu alınır.
  - Sayfa içeriğinde "**bilgisayar**" kelimesi aranır.

⚙️ **Yük Altında Davranış Testi**

- Farklı sanal kullanıcı sayılarıyla test yapılır.
- Yanıt süreleri ve hata oranları gözlemlenir.

---

## 📈 Sonuçların İncelenmesi

- Locust'un **web arayüzü** üzerinden:
  - Yanıt sürelerini
  - Başarı oranlarını
  - Hata yüzdelerini
  detaylıca görebilirsiniz.

- JSON raporları ile **dışa aktarım** yapabilirsiniz.

---

## 🛠 Kullanılan Teknolojiler

- [Locust](https://locust.io/) — Yük Testi Aracı
- Python 3.6+

---

## 📌 Proje Yapısı

```bash
selim-erdinc-load-test/
│
├── main.py         # Test senaryoları
├── README.md       # Proje dökümantasyonu
└── requirements.txt (isteğe bağlı)
```

