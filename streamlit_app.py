import streamlit as st
import pandas as pd
import pickle

# Fungsi untuk halaman penjelasan fitur
def show_feature_info():
    st.title("Penjelasan Fitur Telco Customer Churn")

    st.markdown("""
    #### 1. **Dependents**
    *Apakah pelanggan memiliki tanggungan (anak, pasangan, atau anggota keluarga lain).*
    - **Tipe**: Kategorikal (`Yes` / `No`)

    #### 2. **tenure**
    *Lama pelanggan telah berlangganan (dalam bulan).*
    - **Tipe**: Numerik (`int`)
    - **Contoh nilai**: `1` hingga `72`

    #### 3. **OnlineSecurity**
    *Apakah pelanggan memiliki layanan keamanan online.*
    - **Tipe**: Kategorikal (`Yes`, `No`, `No internet service`)

    #### 4. **OnlineBackup**
    *Apakah pelanggan memiliki layanan backup data online.*
    - **Tipe**: Kategorikal (`Yes`, `No`, `No internet service`)

    #### 5. **InternetService**
    *Jenis layanan internet yang dimiliki pelanggan.*
    - **Tipe**: Kategorikal (`DSL`, `Fiber optic`, `No`)

    #### 6. **DeviceProtection**
    *Apakah pelanggan memiliki perlindungan perangkat.*
    - **Tipe**: Kategorikal (`Yes`, `No`, `No internet service`)

    #### 7. **TechSupport**
    *Apakah pelanggan memiliki dukungan teknis.*
    - **Tipe**: Kategorikal (`Yes`, `No`, `No internet service`)

    #### 8. **Contract**
    *Jenis kontrak langganan pelanggan.*
    - **Tipe**: Kategorikal (`Month-to-month`, `One year`, `Two year`)

    #### 9. **PaperlessBilling**
    *Apakah pelanggan menggunakan tagihan tanpa kertas.*
    - **Tipe**: Kategorikal (`Yes`, `No`)

    #### 10. **MonthlyCharges**
    *Total biaya langganan bulanan pelanggan.*
    - **Tipe**: Numerik (`float`)
    - **Range contoh**: `19` hingga `119`

    #### 11. **Churn (Target Output)**
    *Apakah pelanggan akan berhenti berlangganan.*
    - `1` → Pelanggan **berhenti** (churn)
    - `0` → Pelanggan **tetap** (loyal)
    """)

# Fungsi untuk halaman prediksi churn
def show_prediction():
    st.title("Telco Customer Churn Prediction")

    st.sidebar.header("Input Customer Features")

    def input_user():
        Dependents = st.sidebar.radio("Dependents", ["Yes", "No"])
        tenure = st.sidebar.number_input("Tenure (in months)", min_value=1, max_value=72, value=29, step=1)
        OnlineSecurity = st.sidebar.selectbox("OnlineSecurity", ["Yes", "No", "No internet service"])
        OnlineBackup = st.sidebar.selectbox("OnlineBackup", ["Yes", "No", "No internet service"])
        InternetService = st.sidebar.selectbox("InternetService", ["DSL", "Fiber optic", "No"])
        DeviceProtection = st.sidebar.selectbox("DeviceProtection", ["Yes", "No", "No internet service"])
        TechSupport = st.sidebar.selectbox("TechSupport", ["Yes", "No", "No internet service"])
        Contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
        PaperlessBilling = st.sidebar.radio("PaperlessBilling", ["Yes", "No"])
        MonthlyCharges = st.sidebar.number_input("MonthlyCharges", min_value=19, max_value=119, value=70, step=1)

        data = {
            "Dependents": Dependents,
            "tenure": tenure,
            "OnlineSecurity": OnlineSecurity,
            "OnlineBackup": OnlineBackup,
            "InternetService": InternetService,
            "DeviceProtection": DeviceProtection,
            "TechSupport": TechSupport,
            "Contract": Contract,
            "PaperlessBilling": PaperlessBilling,
            "MonthlyCharges": MonthlyCharges
        }
        return pd.DataFrame([data])

    df_Customer = input_user()
    st.subheader("Customer Feature Preview")
    st.write(df_Customer)

    # Load model
    try:
        model_loaded = pickle.load(open("model_gbc.sav", "rb"))
    except FileNotFoundError:
        st.error("❌ Model file not found!")
        st.stop()

    # Predict
    try:
        pred = model_loaded.predict(df_Customer)[0]
        if pred == 1:
            st.success("✅ **Pelanggan diprediksi BERHENTI (churn).**")
        else:
            st.info("🔒 **Pelanggan diprediksi TETAP berlangganan.**")
    except Exception as e:
        st.error(f"❌ Prediksi gagal: {e}")

# Sidebar navigasi utama
page = st.sidebar.selectbox("Pilih Halaman", ["Beranda", "Prediksi Churn"])

if page == "Beranda":
    show_feature_info()
elif page == "Prediksi Churn":
    show_prediction()
