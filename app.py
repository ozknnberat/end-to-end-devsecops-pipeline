from flask import Flask
import os

app = Flask(__name__)

# 🚨 GÜVENLİK AÇIĞI BURADA! 🚨
# Gerçek projelerde şifreler asla böyle kodun içine AÇIKÇA yazılmaz.
# Biz bunu DevSecOps pipeline'ımızın (Gitleaks) yakalayıp yakalamayacağını test etmek için bilerek yapıyoruz.
# Bu bir "Yem"dir.

DB_USER = "admin"
DB_PASSWORD = "super_secret_password_123" 

@app.route('/')
def hello():
    return "DevSecOps Pipeline Test Uygulamasi Calisiyor!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
