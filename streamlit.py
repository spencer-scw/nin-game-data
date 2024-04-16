import streamlit as st
import pandas as pd
import datetime as dt
from dateutil import parser;

nin_titles = pd.read_csv("Best_Selling_Nintendo_Titles.csv")

nin_titles["Release_Date"] = nin_titles["Release_Date"].apply(parser.parse)

st.multiselect("Which consoles to graph?", options=nin_titles["Console"])

st.line_chart(nin_titles.style, x = "Release_Date", y = "Sales")

year = st.slider("Bestseller by year", 1983, 2023)

nin_titles["Year"] = nin_titles["Release_Date"].apply(lambda x: x.year)

st.write(nin_titles.loc[nin_titles.groupby(["Year"])["Sales"].idxmax()[year]]["Game"])
st.write(nin_titles.loc[nin_titles.groupby(["Year"])["Sales"].idxmax()[year]]["Sales"])