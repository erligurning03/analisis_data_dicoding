## start code
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

# Load data dari csv
# all_df = pd.read_csv("all_data.csv")
url='https://drive.google.com/file/d/11KgQnFSKxX1tir2p6l6HBhsRkFw9QkMV/view?usp=sharing'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
all_df = pd.read_csv(url)



#buat function helper
def get_colors(n):
    colors = sns.color_palette("Blues", n)
    return colors

def create_sum_order_items_df(df, n=15):
    sum_order_items_df = df.groupby("product_category_name").price.sum().sort_values(ascending=False).reset_index()
    return sum_order_items_df.head(n)

def create_state_customer_df(df, n=15):
    by_customer_state_df = df.groupby(by="customer_state").customer_id.nunique().reset_index()
    by_customer_state_df.rename(columns={
        "customer_id": "customer_count"
    }, inplace=True)
    return by_customer_state_df.sort_values(by="customer_count", ascending=False).head(n)

# Load all data CSV
# all_df = pd.read_csv("all_data.csv")

# Create helper functions
sum_order_items_df = create_sum_order_items_df(all_df)
colors = get_colors(len(sum_order_items_df))

# Buat header dashboard
st.header('Dashboard e-commerce-public-dataset')

# Visualisasi data berdasarkann jumlah kategori barang
st.subheader("Kategori Penjualan Produk tertinggi dan Terendah")
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))
sns.barplot(x="price", y="product_category_name", hue="product_category_name", data=sum_order_items_df, palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Kategori Penjualan Tertinggi", loc="center", fontsize=15)
ax[0].tick_params(axis='y', labelsize=12)

sns.barplot(x="price", y="product_category_name", hue="product_category_name", data=sum_order_items_df.sort_values(by="price", ascending=True), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Kategori Penjualan Terendah", loc="center", fontsize=15)
ax[1].tick_params(axis='y', labelsize=12)

plt.suptitle("Kategori Produk Dengan Penjualan Tertinggi Dan Terendah", fontsize=20)
st.pyplot(plt)
plt.clf()

# Visualisasi data berdasarkan negara bagian
st.subheader("Jumlah Pelanggan berdasarkan Negara Bagian ")
state_customer_df = create_state_customer_df(all_df)
colors_ = get_colors(len(state_customer_df))
sns.barplot(x="customer_count", y="customer_state", hue="customer_state", data=state_customer_df, palette=colors_)
plt.title("States Dengan Jumlah Customer Terbanyak", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='y', labelsize=12)
st.pyplot(plt)
plt.clf()

## end of code

