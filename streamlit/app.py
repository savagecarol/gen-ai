import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Streamlit")
st.write("Simple text")


##create dataframe
df = pd.DataFrame({
   'first_co;lumn': [1, 2, 3, 4],
   'second_column': [10, 20, 30, 40]
})

st.write("Here is my dataframe:")
st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)
st.bar_chart(chart_data)
st.area_chart(chart_data)
