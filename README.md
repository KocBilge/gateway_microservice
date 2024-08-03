# Gateway Microservice

Bu proje, mikroservis mimarisi için bir **API Gateway** servisi oluşturmaktadır. Gateway, çeşitli mikroservislere yönlendirme yaparak gelen istekleri yönetir. Bu proje, FastAPI ve HTTPx kullanılarak geliştirilmiştir.

## Özellikler

- **Modüler yapı**: Her mikroservis için bağımsız route ve servis sınıfları.
- **Kolay entegrasyon**: Mikroservis URL'leri `config.py` üzerinden kolayca yapılandırılabilir.
- **Asenkron istekler**: HTTPx kullanarak asenkron iletişim sağlanır.

## Kurulum

Projeyi klonlayın ve gerekli bağımlılıkları yükleyin:

```bash
API Gateway'i çalıştırmak için:
  uvicorn main:app --reload
Projede yer alan testleri çalıştırmak için:
  pytest

git clone https://github.com/KocBilge/gateway_microservice.git
cd gateway_microservice
pip install -r requirements.txt

