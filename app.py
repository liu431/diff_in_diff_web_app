import streamlit as st
import altair as alt
import numpy as np
import pandas as pd
import datetime

from PIL import Image

#from sklearn.linear_model import LinearRegression

st.title("Diff_in_diff app (Demo phrase)")

st.markdown('''Calculate the campaign's impact on sales
''')


with st.sidebar:
    st.write("Select the inputs")
    uploaded_file = st.file_uploader("Choose a file")
    treatment = st.multiselect("Campaign DMAs", ['DMA_1', 'DMA_2', 'DMA_3'])
    control = st.multiselect("Control DMAs", ['DMA_4', 'DMA_5', 'DMA_6'])
    cadence = st.selectbox("Data cadence", ['Daily', 'Weekly'])
    format = st.selectbox("Output format", ['# number', '$ sales'])
    cam_start = st.date_input("When does the campaign start")
    cam_end = st.date_input("When does the campaign end")
    window = st.slider('Post conversion window (When do we run it)', 0, 28, 0)

    
    
    
    st.button('Run')

    # batch = st.slider("What batch size?",min_value=1,max_value=pts,step=1, value = init_batch,
    #             key="batch", on_change = update)

    # step = st.slider("How many updates do you want to perform?",min_value=0,max_value=max_updates,step=1,
    #                 key = "step_slider")


image = Image.open('chart.png')
st.image(image, caption='Output graph')

st.write('''The estimated sales lift during the campaign period is \$217574. Their actual sales during the campaign is \$743234. 
         Without the campaign, the sales would be \$525660 (\$743234 - \$217574).
         The standard error is \$51345 (standard deviation / √n ). 
         The 95% confidence interval is [114453, 320600], meaning that if we were to repeat this multiple times, the lift would fall within this range 95% of the time.
'''
)

