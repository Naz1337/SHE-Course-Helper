import streamlit as st
import pandas as pd
import numpy as np

excel_file = ('C://Users//mfari//Documents//Python Codes//SHE Course Helper//SHE COURSES.xlsx')

st.set_page_config(page_title="SHE Helper!",
                   page_icon=":book:",
                   layout="wide")

she_courses_cluster1 = pd.read_excel(excel_file)

# SIDEBAR
st.sidebar.header("Filtering the SHE course:")
agree = st.sidebar.checkbox('No negatives (DANGEROUS!)', value=True)

learning_mode = st.sidebar.multiselect(
    "Select the Learing Mode:",
    options=she_courses_cluster1["MEDIUM"].unique(),
    default=["ONLINE", "PHYSICAL"]
)

cluster = st.sidebar.selectbox(
    "Select the Cluster:",
    [1, 2, 3, 4]
)

faculty = st.sidebar.multiselect(
    "Select the Faculty:",
    options=she_courses_cluster1["FACULTY"].unique(),
    default=she_courses_cluster1["FACULTY"].unique()
)

full = "F"

if agree:
    df_selection = she_courses_cluster1.query(
    "FACULTY == @faculty & MEDIUM == @learning_mode & FULL == @full & CLUSTER == @cluster & REGISTERED != -1"
)

else:
    df_selection = she_courses_cluster1.query(
        "FACULTY == @faculty & MEDIUM == @learning_mode & FULL == @full & CLUSTER == @cluster"
    )



## MAINPAGE
st.title(":book: SHE Course Helper!")
st.subheader("By Faris Faiz and Faiqah Azman")

vacant_courses = she_courses_cluster1['FULL'].value_counts()['F']

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Available Courses:")
    st.subheader(len(she_courses_cluster1))

with middle_column:
    st.subheader("Vacant Courses:")
    st.subheader(vacant_courses)

she_courses_cluster1.groupby(by=["FULL"]).sum()

st.title("List of Available Courses:")
st.subheader("Any -1 Values mean it's unknown, Registered means people have registered for the subject, Capacity is the capacity of the subject. \nIt's better to focus on the subjects that don't have any negative numbers!")
st.dataframe(df_selection)