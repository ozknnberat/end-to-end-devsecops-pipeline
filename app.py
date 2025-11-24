from flask import Flask
import os

app = Flask(__name__)

# ✅ GÜVENLİ YÖNTEM:
# Şifreler kodun içinde değil, ortam değişkenlerinde (Environment Variables) saklanır.
# Eğer şifre yoksa boş döner, kod patlamaz ama şifre de ifşa olmaz.
DB_USER = os.environ.get("DB_USER", "admin")
DB_PASSWORD = os.environ.get("DB_PASSWORD") 

@app.route('/')
def hello():
    return "Guvenli DevSecOps Uygulamasi - Security Check Passed! ✅"

if __name__ == '__main__':
    # ✅ GÜVENLİ YÖNTEM:
    # 0.0.0.0 yerine 127.0.0.1 kullanarak sadece local erişime izin verdik.
    # Bandit artık hata vermeyecek.
    app.run(host='127.0.0.1', port=5000)
