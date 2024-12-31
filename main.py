import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


st.title('My first app')

st.write("Display Image")

option = st.selectbox('好きな数字', list(range(1, 11)))

'You selected:', option 


# if st.checkbox('Show Image'):
#     img = Image.open("2022-07-31.png")
#     st.image(img, caption="2022-07-31", use_container_width=True)





# df = pd.DataFrame(
#     np.random.rand(100, 2)/[5,5] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# #st.table(df.style.highlight_max(axis=0))
# st.map(df)


