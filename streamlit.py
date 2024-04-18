import streamlit as st
import pandas as pd
import datetime as dt
from dateutil import parser;

st.title("Nintendo Game Data Exploration!")

nin_titles = pd.read_csv("Best_Selling_Nintendo_Titles.csv")

nin_titles["Release_Date"] = nin_titles["Release_Date"].apply(parser.parse)

consoles = st.multiselect("Which consoles to graph?", options=nin_titles["Console"].unique())

con_mask = [value in consoles for value in nin_titles["Console"].values]
con_nin_titles = nin_titles
con_nin_titles["Mask"] = con_mask

st.line_chart(con_nin_titles.loc[nin_titles["Mask"]].style, x = "Release_Date", y = "Sales")

year = st.slider("Bestseller by year", 1983, 2023)

nin_titles["Year"] = nin_titles["Release_Date"].apply(lambda x: x.year)

st.write(
    " The bestseller for " + str(year) + " was " +
    nin_titles.loc[nin_titles.groupby(["Year"])["Sales"].idxmax()[year]]["Game"] + 
    ", with " +
    str(round(nin_titles.loc[nin_titles.groupby(["Year"])["Sales"].idxmax()[year]]["Sales"] / 1000000, ndigits=2)) +
    " million copies sold."
    )

with st.sidebar:
    filter = st.text_input("Filter the data by games containing:")

    mask = [filter in value for value in nin_titles["Game"].values]
    filter_nin_titles = nin_titles
    filter_nin_titles["Mask"] = mask
    filter_nin_titles = filter_nin_titles.loc[filter_nin_titles["Mask"]].drop("Mask", axis=1)

    st.write(
        filter_nin_titles
    )

    st.write(
        "Matched a total of " + str(filter_nin_titles.shape[0]) + " games."
    )

    st.write(
        "The mean sales for the games containing '" + filter + "' is " + str(round(filter_nin_titles["Sales"].mean() / 1000000, ndigits=2)) + " million."
    )

    st.write(
        "The bestselling game containing '" + filter + "' is " +
        filter_nin_titles.sort_values(by="Sales", ascending=False).iloc[0]["Game"] +
        " with a total of " + str(round(filter_nin_titles.sort_values(by="Sales", ascending=False).iloc[0]["Sales"] / 1000000, ndigits=2)) + " million copies sold."
    )