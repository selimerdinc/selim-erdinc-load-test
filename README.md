# N11 Arama Modülü Yük Testi

Bu proje, Locust kullanarak N11’in arama modülünün yük altındaki davranışını test etmeyi amaçlamaktadır. Bu doküman, testlerin kurulumunu ve çalıştırılmasını açıklamaktadır.

## Gereksinimler
- Python 3.6+
- pip (Python paket yöneticisi)

## Proje Kurulumu

1. **Proje dizininizi oluşturun ve içine geçiş yapın:**
    ```bash
    mkdir n11-search-load-test
    cd n11-search-load-test
    ```

2. **Locust dosyasını oluşturun:**
    `main.py` adında bir dosya oluşturun ve aşağıdaki kodu yapıştırın:

3. **Bağımlılıkları yükleyin:**
    ```bash
    pip install locust
    ```

4. **Testi başlatın:**
    ```bash
    locust -f main.py --users 100 --spawn-rate 10 --host https://www.n11.com 
    ```

5. **Web arayüzünü kullanarak testi yapılandırın:**
    - Tarayıcınızda `http://localhost:8089` adresini açın.
    - Kullanıcı sayısı (Number of users) ve bağlanma hızını (Spawn rate) belirleyerek testi başlatın.

## Test Senaryosu

1. **Arama Çubuğu Testi:**
    - `/arama?q=bilgisayar` endpoint’i kullanılarak, "bilgisayar" kelimesi için arama yapılır.
    - Gelen yanıtta "bilgisayar" kelimesinin varlığı ve HTTP durum kodunun 200 olduğu kontrol edilir.

2. **Yük Altında Davranış Testi:**
    - Farklı sayılarda sanal kullanıcılarla arama modülü test edilir.
    - Yanıt süreleri ve hata oranları izlenir.

## Sonuçları Analiz Etme
- Test sonucunda, yanıt süreleri ve hata durumları hakkında bilgi sahibi olunabilir.
- Test sonuçlarını web arayüzünde veya Locust’un sunduğu JSON raporları aracılığıyla inceleyebilirsiniz.


Bu proje, N11’in arama modülü üzerinde daha iyi bir performans analizi yapmaya yönelik bir yaklaşım sunmaktadır.

