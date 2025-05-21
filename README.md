# Telco Customer Churn Prediction


## Latar Belakang
Manajemen Pemasaran sebuah perusahaan telekomunikasi menghadapi tantangan besar terkait tingkat churn pelanggan yang cukup tinggi. Mereka selama ini mengeluarkan biaya promosi ke seluruh pelanggan tanpa tahu siapa yang benar-benar berisiko berhenti menggunakan layanan. Strategi ini tidak efisien, karena sebagian besar promosi justru jatuh kepada pelanggan loyal yang sebenarnya tidak berniat berhenti.

Sebagai Data Scientist perusahaan, diberi tugas oleh Manajemen Pemasaran untuk mengembangkan model machine learning yang mampu memprediksi apakah seorang pelanggan akan melakukan churn atau tidak. Dengan model ini, diharapkan perusahaan:
- Dapat mengidentifikasi pelanggan yang berpotensi churn sebelum mereka benar-benar pergi.
- Dapat mengoptimalkan biaya promosi, hanya diberikan kepada pelanggan yang benar-benar membutuhkan.
- Dapat mengurangi kerugian dari kehilangan pelanggan setia.

## Metric Evaluation
- Cost FP: $100
- Cost FN: $500

False Positive (FP): Model memprediksi seorang customer akan churn → perusahaan memberi promosi senilai $100, tetapi sebenarnya customer tidak churn.
→ Biaya promosi sia-sia.

False Negative (FN): Model memprediksi customer tidak akan churn → perusahaan tidak melakukan tindakan, tetapi sebenarnya customer churn.
→ Perusahaan kehilangan customer dengan potensi kerugian $500.

Karena cost dari FN jauh lebih tinggi dibanding FP, karena itu F2-score dipilih sebagai metrik evaluasi utama, karena F2-score memberikan lebih banyak bobot ke recall.

## Tujuan/ Goals
1. Memprediksi Churn Pelanggan
Mengembangkan model Machine Learning yang dapat mengidentifikasi pelanggan yang berpotensi churn (berhenti berlangganan) berdasarkan data historis pelanggan.

2. Mengurangi Kerugian Finansial
Membantu perusahaan mengurangi biaya akibat kehilangan pelanggan (False Negative) yang memiliki dampak finansial besar ($500 per pelanggan) dengan memberikan penanganan preventif.

3. Mengoptimalkan Strategi Promosi
Mengurangi pemborosan promosi kepada pelanggan loyal (False Positive) yang sebenarnya tidak akan churn ($100 per pelanggan) dengan hanya menargetkan pelanggan yang benar-benar berisiko churn.

4. Menggunakan Metode Evaluasi yang Tepat
Menggunakan metrik F2 Score sebagai acuan utama untuk mengevaluasi model, karena memberikan penekanan lebih besar pada minimisasi False Negative.

5. Memberikan Insight Fitur Penting
Mengidentifikasi fitur-fitur yang paling berkontribusi terhadap keputusan churn agar perusahaan dapat melakukan intervensi bisnis yang lebih tepat sasaran (misalnya melalui peningkatan layanan atau paket berlangganan).


## Telco Customer Churn Prediction App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dp-machinelearning-kh.streamlit.app/)
## GitHub Codespaces

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/kahfidwi/dp-machinelearning/tree/master)
