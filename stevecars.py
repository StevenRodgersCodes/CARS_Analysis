import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv("CARS.csv")
    df.MSRP = df.MSRP.replace("[$,]", "", regex=True).astype('int64')
    return df

df = load_data()

# App title
st.title("Car MSRP Visualization by Make and Type")

# Sidebar selections
make = st.sidebar.selectbox("Select Car Make", sorted(df.Make.unique()))
filtered_make_df = df[df.Make == make]

car_type = st.sidebar.selectbox("Select Car Type", sorted(filtered_make_df.Type.unique()))
filtered_df = filtered_make_df[filtered_make_df.Type == car_type]

# Show bar chart
st.subheader(f"MSRP of {make} - {car_type} Models")

if not filtered_df.empty:
    plt.figure(figsize=(12, 6))
    sb.barplot(x=filtered_df.Model, y=filtered_df.MSRP, palette='ocean')
    plt.xticks(rotation=90)
    st.pyplot(plt.gcf())
else:
    st.warning("No data available for the selected combination.")
