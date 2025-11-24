# 🛡️ End-to-End DevSecOps Pipeline

![Build Status](https://github.com/ozknnberat/end-to-end-devsecops-pipeline/actions/workflows/main.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Security](https://img.shields.io/badge/Security-Shift%20Left-green)

Bu proje, modern yazılım geliştirme süreçlerinde **güvenliği** en başa taşıyan (Shift-Left) kapsamlı bir **CI/CD (Sürekli Entegrasyon/Sürekli Dağıtım)** hattını simüle eder.

Amaç, güvensiz kodun (şifre ifşası veya hatalı konfigürasyon) canlı ortama geçmesini **otomasyon** ile engellemektir.

## 🚀 Proje Mimarisi

Bu pipeline, kod GitHub'a gönderildiği anda otomatik olarak tetiklenir ve aşağıdaki güvenlik kontrollerinden geçer:

```mermaid
graph LR
    A["Geliştirici Commit"] --> B{"GitHub Actions"}
    B --> C["🔑 Secret Scanning (Gitleaks)"]
    C -- "Şifre Bulundu" --> F["⛔ Pipeline FAIL"]
    C -- "Temiz" --> D["🐍 SAST Analizi (Bandit)"]
    D -- "Hata Bulundu" --> F
    D -- "Temiz" --> E["🚀 Fake Deploy (Success)"]
    
Araç,Kategori,Kullanım Amacı
GitHub Actions,CI/CD,Otomasyon süreçlerini ve pipeline yönetimini sağlar.
Python (Flask),Uygulama,Güvenlik testlerinin yapıldığı örnek web uygulaması.
Gitleaks,Secret Scanning,Kod içinde unutulan API anahtarları ve şifreleri tarar.
Bandit,SAST,Python kodundaki güvenlik açıklarını (örn. 0.0.0.0 binding) tespit eder.

