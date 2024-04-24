import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us_fixed.csv')

st.title('SDT Project')
st.write('This web app compares statistics from a car ad hosting site')

year_1 = st.checkbox('Cars posted in 2018', value=True)
year_2 = st.checkbox('Cars posted in 2019', value=True)



if year_1:
    df = df[df['date_posted_year'] == 2018]
if year_2:
    df = df[df['date_posted_year'] == 2019]

odometer_condition = px.scatter(df, x='vehicle_age', y='odometer', color='condition', opacity=.7)
manufacturer_stats = px.histogram(df, x='type', color='manufacturer')
days = px.histogram(df, x='days_listed', color='condition')
price = px.scatter(df, x='date_posted', y='price', color='condition', opacity=.7)

st.plotly_chart(odometer_condition)
st.plotly_chart(manufacturer_stats)
st.plotly_chart(days)
st.plotly_chart(price)