import matplotlib.pyplot as plt
import numpy as np
import streamlit as ss
import pandas as pd

# sidebar
ss.text("Nama: Carloka Boas Alberto Sembiring Meliala" )
ss.title('Data Wrangling')

# Tabsgit init
Gathering_Data, Assessing_Data, Cleaning_Data = ss.tabs(["Gathering Data", "Assessing Data", "Cleaning Data"])
 
with Gathering_Data:
    tab1, tab2 = ss.tabs(["1", "2"])
    with tab1:
        ss.text("dataset hour")
        df = pd.read_csv("data/hour.csv", delimiter=",")    
        ss.dataframe(df)
    with tab2:
        ss.text("dataset day")
        df = pd.read_csv("data/day.csv", delimiter=",")    
        ss.dataframe(df)
    

with Assessing_Data:
    tab1, tab2 ,tab3= ss.tabs(["1", "2","3"])
    with tab1:
        ss.title("Analisis Data Penyewaan Sepeda")
        hours_df = pd.read_csv("data/hour.csv")
        ss.subheader("Jumlah Duplikasi:")
        ss.write(hours_df.isna().sum())
        ss.subheader("Nilai Unik dalam Kolom 'weathersit':")
        ss.write(hours_df['weathersit'].unique())
    with tab2:
        ss.title("Analisis Data Penyewaan Sepeda")
        day_df = pd.read_csv("data/day.csv")
        jumlah_duplikat = day_df.duplicated().sum()
        ss.subheader("Jumlah Data Duplikat:")
        ss.write(jumlah_duplikat)
        
    with tab3:
        ss.title("Analisis Data Penyewaan Sepeda")
        day_df = pd.read_csv("data/day.csv")
        jumlah_nilai_hilang = day_df.isnull().sum()
        ss.subheader("Jumlah Nilai yang Hilang di Setiap Kolom:")
        ss.write(jumlah_nilai_hilang)
 
with Cleaning_Data:
     tab1, tab2= ss.tabs(["1", "2"])
     with tab1:
         ss.title("Analisis Data Penyewaan Sepeda")
         hour_df = pd.read_csv("data/hour.csv")
         hour_df.drop_duplicates(inplace=True)
         hour_df.drop(columns=['instant'], inplace=True)
         ss.subheader("Data Penyewaan Sepeda per Jam:")
         ss.dataframe(hour_df.head())
         
     with tab2:
         ss.title("Analisis Data Penyewaan Sepeda")
         day_df = pd.read_csv("data/day.csv")
         day_df.drop_duplicates(inplace=True)
         day_df['dteday'] = pd.to_datetime(day_df['dteday'], dayfirst=True)
         ss.subheader("Data Penyewaan Sepeda per Hari:")
         ss.dataframe(day_df.head())
         

ss.title('Exploratory Data Analysis (EDA)')
Tab1,Tab2,Tab3 = ss.tabs(["1", "2", "3"])
with Tab1:
    ss.title("Analisis Data Penyewaan Sepeda per Musim")
    day_df = pd.read_csv("data/day.csv")
    ss.subheader("Tipe Data dari Setiap Kolom:")
    ss.write(day_df.dtypes)
    day_df = day_df.drop(columns=['dteday'])
    numeric_columns = day_df.select_dtypes(include='number').columns
    average_by_season = day_df.groupby(by="season")[numeric_columns].mean()
    ss.subheader("Rata-Rata Data Penyewaan per Musim:")
    ss.dataframe(average_by_season)
with Tab2:
    ss.title("Analisis Data Penyewaan Sepeda per Jam")
    hour_df = pd.read_csv("data/hour.csv")
    ss.subheader("Histogram Data Penyewaan Sepeda per Jam:")
    hour_df.hist(bins=30, figsize=(10, 8), grid=False)
    plt.tight_layout() 
    ss.pyplot(plt)
    hour_df_numeric = hour_df.select_dtypes(include=['number'])
    ss.subheader("Matriks Korelasi:")
    correlation_matrix = hour_df_numeric.corr()
    ss.dataframe(correlation_matrix)
    

with Tab3:
    day_df = pd.read_csv("data/day.csv")
    ss.title("Analisis Data Penyewaan Sepeda per Hari")
    ss.subheader("Ringkasan Statistik Data:")
    stats_summary = day_df.describe(include="all")  
    ss.dataframe(stats_summary)  
    
ss.title("Visualization & Explanatory Analysis")
Pertanyaan1 , Pertanyaan2, = ss.tabs([' Berapa Jumlah penyewaan sepeda yang dihasilkan untuk setiap musim?', 'Berapa Jumlah penyewaan sepeda untuk per jam-nya?'])
with Pertanyaan1:
    day_df = pd.read_csv("data/day.csv")
    season_counts = day_df.groupby('season')['cnt'].sum()
    plt.figure(figsize=(10, 6))
    season_counts.plot(kind='bar', color='skyblue')
    plt.title('Jumlah Penyewa Sepeda Berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Penyewa')
    plt.xticks(ticks=[0, 1, 2, 3], labels=['Musim Dingin', 'Musim Semi', 'Musim Panas', 'Musim Gugur'], rotation=0)
    plt.grid(axis='y')

    ss.title("Analisis Jumlah Penyewa Sepeda Berdasarkan Musim")
    ss.pyplot(plt) 

with Pertanyaan2:
    hour_df = pd.read_csv("data/hour.csv")

    ss.title('Analisis Penyewaan Sepeda per Jam')

    ss.write("Visualisasi ini menampilkan jumlah penyewa sepeda di setiap jam berdasarkan dataset yang tersedia.")

    def plot_rental_per_hour():
        plt.figure(figsize=(12, 6))
        plt.bar(hour_df['hr'], hour_df['cnt'], color='skyblue')
        plt.title('Jumlah Penyewa Sepeda per Jam', fontsize=16)
        plt.xlabel('Jam', fontsize=12)
        plt.ylabel('Jumlah Penyewa', fontsize=12)
        plt.xticks(range(0, 24)) 
        plt.grid(axis='y', linestyle='--', alpha=0.7)  
        ss.pyplot(plt)  
    plot_rental_per_hour()     
    
ss.title("Analisis Lanjutan")
RFM_Analysis,Geospatial_Analysis,Clustering = ss.tabs(["RFM Analysis", "Geospatial Analysis", "Clustering"])
with RFM_Analysis:
    ss.title("Analisis RFM Penyewaan Sepeda")
    day_df = pd.read_csv("data/day.csv")
    day_df['total_rentals'] = day_df['casual'] + day_df['registered']
    rfm_df = day_df.groupby('dteday').agg(
        Recency=('dteday', lambda x: (pd.to_datetime('2012-12-31') - pd.to_datetime(x)).dt.days.min()),
        Frequency=('total_rentals', 'sum'),
        Monetary=('total_rentals', 'sum')
    ).reset_index()

    ss.subheader("Hasil RFM")
    ss.dataframe(rfm_df)
    
with Geospatial_Analysis:
    ss.title("Distribusi Penyewa Sepeda berdasarkan Lokasi")
    day_df = pd.read_csv("data/day.csv")
    ss.subheader("Nama Kolom dalam Dataset:")
    ss.write(day_df.columns)
    day_df['longitude'] = -77.0369  # Contoh longitude
    day_df['latitude'] = 38.9072    # Contoh latitude
    plt.figure(figsize=(12, 8))
    plt.scatter(day_df['longitude'], day_df['latitude'], c=day_df['cnt'], cmap='viridis', alpha=0.6, edgecolors='w', s=100)
    plt.colorbar(label='Jumlah Penyewa')
    plt.title('Distribusi Penyewa Sepeda berdasarkan Lokasi')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid()
    ss.pyplot(plt)

with Clustering:
    ss.title("Analisis Penyewaan Sepeda - Clustering")
    day_df = pd.read_csv("data/day.csv")
    day_df['Rental_Category'] = pd.cut(day_df['cnt'], bins=[0, 100, 300, float('inf')], labels=['Rendah', 'Sedang', 'Tinggi'])

# melAkukan binning
    day_df['Rental_Bin'] = pd.cut(day_df['cnt'], bins=[0, 100, 300, 500, 700, 900, 1100], labels=['0-100', '100-300', '300-500', '500-700', '700-900', '900-1100'], right=False)
    ss.subheader("Jumlah Penyewa Berdasarkan Kategori")
    category_counts = day_df['Rental_Category'].value_counts()

    plt.figure(figsize=(12, 6))
    category_counts.plot(kind='bar', color='skyblue', alpha=0.7)
    plt.title('Jumlah Penyewa Berdasarkan Kategori')
    plt.xlabel('Kategori Penyewa')
    plt.ylabel('Jumlah Hari')
    plt.xticks(rotation=0)
    plt.grid(axis='y')

    ss.pyplot(plt)

with ss.expander("Conclusion"):
    ss.write(
        """Kesimpulan Pertanyaan 1: Analisis menunjukkan bahwa kondisi cuaca berpengaruh signifikan terhadap jumlah penyewaan sepeda. Pada jam sibuk, suhu yang lebih tinggi cenderung meningkatkan jumlah penyewa, karena orang lebih suka bersepeda dalam cuaca yang nyaman. Namun, selama jam tidak sibuk, faktor lain seperti hujan atau angin dapat menurunkan minat bersepeda\n.
Kesimpulan Pertanyaan 2: Terdapat perbedaan yang jelas antara penyewaan sepeda pada hari kerja dan akhir pekan. Hari kerja umumnya menunjukkan jumlah penyewa yang lebih tinggi, terutama selama jam sibuk, karena orang menggunakan sepeda untuk keperluan transportasi. Sebaliknya, pada akhir pekan, meskipun penyewaan cenderung lebih rendah di pagi hari, jumlah penyewa meningkat saat orang menggunakan sepeda untuk rekreasi, terutama di siang dan sore hari.
        """
    )