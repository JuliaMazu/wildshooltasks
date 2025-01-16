import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


list_datasets = sns.get_dataset_names()

st.header("Data manipulation and dataviz")

st.write("Which dataset are we going to use?")
dataset  = st.selectbox("", list_datasets)

df = sns.load_dataset(dataset)

st.dataframe(df.head(20))

x_axis  = st.selectbox("Now I want you to chose X axis", df.columns)
y_axis  = st.selectbox("Without Y axis there is no fun. Please chose it as well", df.columns)
graph = st.selectbox("Which type of graph are we going to use", 
                          ["bar", "scatter", "line"])

eval(f"st.{graph}_chart(df, x = x_axis, y = y_axis)")   

matrix = st.checkbox('Do you want me to show you correlation matrix?')
if matrix:
    if (df[x_axis].dtype in ["float64", "int64"]) and (df[y_axis].dtype in ["float64", "int64"]):
        sns.heatmap(df[[f"{x_axis}", f"{y_axis}"]].corr(),  annot=True)
        st.pyplot(plt.gcf())

    else:
        st.markdown(f"#### :red[You need to chose numeric columns. Chose between these {df.select_dtypes(['float64', 'int64']).columns.values}]")