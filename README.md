# KLASIFIKASI-EMOSI-PADA-TEKS-MEDIA-SOSIAL-X-TWITTER-INDONESIA-MENGGUNAKAN-METODE-NEURAL-NETWORK

# Analisis Emosi di Twitter Menggunakan Simple RNN dan Word2Vec

Proyek ini bertujuan untuk menganalisis emosi pada tweet menggunakan model Simple RNN dan representasi kata Word2Vec, berdasarkan metodologi KDD (Knowledge Discovery in Databases).

## Tahapan KDD

### 1. Pemahaman Domain (Domain Understanding)
**Tujuan:** Menentukan tujuan analisis dan memahami konteks serta kebutuhan data.
- Menentukan pertanyaan penelitian atau tujuan bisnis.
- Memahami masalah yang akan diselesaikan dan bagaimana data dapat membantu.
- Mengidentifikasi jenis data yang dibutuhkan dan sumber data yang relevan.

### 2. Pengumpulan Data (Data Collection)
**Tujuan:** Mengumpulkan data yang relevan dari berbagai sumber.
- Mengakses dan mengumpulkan data dari database internal, API eksternal, web scraping, file CSV, dll.
- Mengumpulkan data historis dan data real-time sesuai kebutuhan.
- Memastikan data mencakup semua variabel yang diperlukan untuk analisis.

### 3. Integrasi Data (Data Integration)
**Tujuan:** Menggabungkan data dari berbagai sumber menjadi satu set data yang konsisten dan kaya informasi.
- Menggabungkan data dari berbagai sumber.
- Menyelaraskan format data yang berbeda (misalnya, format tanggal, format teks, tipe data numerik).
- Menangani ketidakkonsistenan data seperti duplikasi, data yang hilang (missing values), atau data yang bertentangan.
- Menambahkan atribut baru yang relevan untuk memperkaya dataset.

### 4. Exploratory Data Analysis (EDA)
**Tujuan:** Memahami karakteristik dan struktur data secara mendalam.
- Menghitung statistik dasar seperti mean, median, mode, dan standard deviation.
- Membuat visualisasi data seperti histogram, box plot, scatter plot, dan heatmap untuk melihat distribusi dan hubungan antar variabel.
- Menganalisis korelasi antar variabel untuk menemukan hubungan yang signifikan.
- Mengidentifikasi pola, anomali, dan wawasan awal yang membantu dalam tahap berikutnya.

### 5. Pra-pemrosesan Data (Data Preprocessing)
**Tujuan:** Membersihkan dan menyiapkan data untuk analisis lebih lanjut.
- Case Folding: Mengubah semua karakter dalam teks menjadi huruf kecil untuk konsistensi.
- Cleansing: Membersihkan teks dari karakter atau elemen yang tidak diperlukan seperti tanda baca, angka, atau simbol lain yang tidak relevan.
- Normalization: Mengubah kata-kata atau frasa ke dalam bentuk yang konsisten.
- Stopword Removal: Menghapus kata-kata umum yang tidak memiliki makna penting dalam analisis teks.
- Stemming: Mengubah kata ke dalam bentuk dasar atau akar katanya.
- Tokenization: Memecah teks menjadi unit-unit kecil seperti kata atau token.
- Padding: Menambahkan padding pada urutan token untuk memastikan semua input memiliki panjang yang sama.

### 6. Transformasi Data (Data Transformation)
**Tujuan:** Mengubah data ke dalam format yang sesuai untuk data mining.
- Mengubah teks menjadi representasi vektor (misalnya, menggunakan Word2Vec).
- Normalisasi fitur-fitur numerik jika diperlukan.
- **Pembagian Dataset (Data Splitting):** Membagi data yang telah diproses menjadi data training, data validation, dan data testing.
  - Data Training: Digunakan untuk melatih model (70-80% dari total data).
  - Data Validation: Digunakan untuk validasi selama pelatihan model untuk menghindari overfitting (10-15% dari total data).
  - Data Testing: Digunakan untuk menguji kinerja akhir model setelah pelatihan selesai (10-15% dari total data).

### 7. Data Mining
**Tujuan:** Menerapkan algoritma dan teknik data mining untuk menemukan pola.
- Melatih model machine learning atau deep learning dengan data yang telah diproses dan ditransformasikan.
- Menggunakan algoritma seperti RNN untuk klasifikasi emosi.
- Melakukan validasi dan tuning model untuk meningkatkan kinerja.

### 8. Evaluasi Pola (Pattern Evaluation)
**Tujuan:** Mengevaluasi hasil data mining.
- Mengevaluasi kinerja model menggunakan metrik seperti akurasi, precision, recall, dan F1-score.
- Membandingkan hasil model dengan baseline atau metode lain jika ada.
- Mengidentifikasi kekuatan dan kelemahan model serta area untuk perbaikan.

### 9. Representasi Pengetahuan (Knowledge Representation)
**Tujuan:** Menyajikan hasil analisis dalam format yang dapat dimengerti dan berguna.
- Membuat visualisasi hasil seperti grafik dan tabel yang mudah dipahami.
- Menyusun laporan atau presentasi yang menjelaskan temuan dan implikasinya.
- Menyediakan rekomendasi berdasarkan hasil analisis untuk pengambilan keputusan.
