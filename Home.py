import streamlit as st
import streamlit.components.v1 as components
import base64
from PIL import Image
import io

import streamlit as st





motion = """
    <style>
        @keyframes slide {
            0% { transform: translateX(0%); }
            100% { transform: translateX(100%); }
        }

        .motion-text {
            white-space: nowrap;
            overflow: hidden;
             
            animation: slide 10s linear infinite;
        }color: #C3ACD0; /* Change the text color */
            font-family: Arial, sans-serif;
    </style>
"""

# Streamlit app
st.markdown(motion, unsafe_allow_html=True)

# Display motion text
st.markdown('<div class="motion-text">Welcome to</div>', unsafe_allow_html=True)

#st.set_page_config( page_title = "this is a multipage")
#st.write("hi ", unsafe_allow_html=True)
#st.write(" # MENTAL MENTOR ", unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 




with open("C:\Users\HP\OneDrive\Desktop\UIT-MentalMentor\front.png", "rb") as f:
    img_content = f.read()

# Load image using PIL (Python Imaging Library)
image = Image.open(io.BytesIO(img_content))

# Define desired width and height for the image
width = 2500  # Set your desired width
height = 1900  # Set your desired height

# Resize the image
resized_image = image.resize((width, height))

# Display the resized image in Streamlit
st.image(resized_image, caption='mind is wealth', use_column_width=True)


  
#with open("front.png", "rb") as f:
 #   img_content = f.read()
  #  data_url = base64.b64encode(img_content).decode("utf-8")

   # width = 1500
    #height = 1300

    #resized_image = img_content.resize((width, height))


    #st.markdown(
     #   f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    #unsafe_allow_html=True,
    #)



