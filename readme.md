# 🌱 FastAPI - Pencarian Berita Sayuran dari Google News RSS

Proyek ini adalah API sederhana berbasis **FastAPI** untuk mencari berita dengan kata kunci tertentu (misalnya: "sayuran") dari **Google News RSS**.

---

## 📦 Fitur Utama

- 🔍 Endpoint `/search?q=kata_kunci` untuk mencari berita dari Google News RSS.
- 🌐 Mengambil data dari RSS feed Google News (berbahasa Indonesia).
- ⚡ Cepat dan ringan, cocok untuk backend aplikasi berita, riset NLP, atau sistem rekomendasi.

---

## 🗂️ Struktur Folder

api_nlp_ir/
├── app/
│ ├── main.py # Entry point FastAPI
│ ├── routes/
│ │ └── news.py # Endpoint pencarian berita
│ ├── services/
│ │ └── rss_feed.py # Logic untuk fetch & parsing RSS
│ ├── core/
│ │ └── config.py # Konfigurasi RSS URL
│ └── init.py
├── requirements.txt # Daftar dependensi Python
└── README.md # Dokumentasi proyek

yaml
Copy
Edit

---

## 🚀 Cara Menjalankan

### 1. Clone Repositori
git clone https://github.com/username/fastapi-berita-rss.git
cd fastapi-berita-rss

2. Buat Virtual Environment (Opsional tapi Disarankan)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Install Dependensi
pip install -r requirements.txt

4. Jalankan Server
uvicorn app.main:app --reload

5. Coba di Browser atau Postman
http://127.0.0.1:8000/search?q=sayuran