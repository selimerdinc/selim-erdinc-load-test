from locust import HttpUser, task, between


class N11SearchTest(HttpUser):
    wait_time = between(1, 3)
    host = "https://www.n11.com"

    @task
    def search_computer(self):
        response = self.client.get("/arama?q=bilgisayar", headers={"User-Agent": "Mozilla/5.0"})
        print(f"Status code: {response.status_code}")
        print(response.text[:500])

        if response.status_code == 200 and "bilgisayar" in response.text.lower():
            print("Arama sonuçları doğru şekilde yüklendi.")
        else:
            print("Hata: Arama sonuçları bekleneni karşılamadı.")