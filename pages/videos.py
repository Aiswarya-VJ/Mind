import streamlit as st
import streamlit.components.v1 as components
import base64

st.title("Videos To Care Your Mind")
st.write("Here are some relaxing videos on how to calm your mind.Go through this videos so you could familiarise with the common suitations and issues face by majority and how to manage them. ")
st.subheader('Stress and Tension:')
st.video("https://youtu.be/yGTArUjtHr0?si=JTQN7B4LQYVEdgFv")
st.video("https://youtu.be/iqcAWup2aCE?si=-0kI1vLNDznGJWAi")
st.video("https://youtu.be/z6X5oEIg6Ak?si=yrBvTxhqELmE-lNe")
st.video("https://youtu.be/ZsJ9utjAqZU?si=YQI0Gj1zxqqRvmIN")
st.video("https://youtu.be/ZsJ9utjAqZU?si=UcHJT_pylztSIjUt")
st.video("https://youtu.be/5zhnLG3GW-8?si=fab2gFo-3zQNh5da")
st.subheader('Anger issues:')
st.video("https://youtu.be/BsVq5R_F6RA?si=iIK97VBmFCm651Yu")
st.video("https://youtu.be/tV2Ecd7m6Tc?si=fBgpbNYjWVc-07pz")
st.video("https://youtu.be/C1N4f1F0vDU?si=IvTs0w_TRfZ0l-i3")
st.video("https://youtu.be/zpucCXdOSH8?si=vB0qTCRa7rVL9v8O")
st.video("https://youtu.be/LNengFfaVGE?si=dCQxPDSmOflV5HCx")
st.video("https://youtu.be/d_5DU5opOFk?si=3saV5TbO2N3bPXmt")
st.video("https://youtu.be/20Yhh2jQxxM?si=1iv7goxzGx06K5ae")
st.subheader('Anxiety:')
st.video("https://youtu.be/McCDfP5M878?si=IuPZs6jFyBauXsmo")
st.video("https://youtu.be/5zhnLG3GW-8?si=85GwEaaS43-vtgDd")
st.video("https://youtu.be/BglgioFwmMc?si=lnkfKAJg4PoPkV-3")
st.video("https://youtube.com/shorts/2QZUJBGfY4s?si=zQjUBUASFB4mdbJe")
st.video("https://youtube.com/shorts/S7XOnZDqMWM?si=vuatZzh-Y9ZS7bgq")
st.video("https://youtube.com/shorts/ceq5lOKnqIk?si=gpSiRCCZzq7i8Ahp")
st.video("https://youtube.com/shorts/UnJiweJ9064?si=E6_6Iyxqi3yYsiBT")
st.subheader('Fear:')
st.video("https://youtu.be/mBjaYVKgV_w?si=uroE_XotX6myrbz3")
st.video("https://youtu.be/tSmSbZg3Lzo?si=vlTrzpp3neS4gn9j")
st.video("https://youtu.be/ubSWWqDpldE?si=a-KI_84ixpRsfJX3")
st.video("https://youtu.be/s_jaJlyNreM?si=yTIRzA953o_rYcQA")
st.video("https://youtu.be/cgMvFRUAd0s?si=CbLA_yplIWn5xcmz")
st.video("https://youtu.be/godVDNVWeso?si=FJZb4C1CodZq4wq3")
st.video("https://youtu.be/hUA_k76x2uE?si=4Ck4RqHFFhim1-Ic")
st.subheader('Depressed:')
st.video("https://youtu.be/29DXrS0bBcU?si=Lwa9mr6GpDaBkYmJ")
st.video("https://youtu.be/Y9A5wuTtblw?si=HHfdhCq1n6H6lUsv")
st.video("https://youtu.be/8WtAA8daRr8?si=thxc762vhRgpGDwe")
st.video("https://youtu.be/WDiLJJ753ww?si=ElTC40nxX6RbSVSl")
st.video("https://youtu.be/VlDgowUAyx4?si=oxdXEsgBb14j_T4H")
st.video("https://youtu.be/859TCiFeKZ8?si=kTzGkUz05IHAHKaf")



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
gif_path = 'pages\image.json'  # Replace this with the path to your GIF file

#with open(r"C:\Users\HP\OneDrive\Desktop\mental-health-care-main\pages\Relax.py", "rb") as f:
 #   img_content = f.read()
  #  data_url = base64.b64encode(img_content).decode("utf-8")

   # st.markdown(
    #    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    #unsafe_allow_html=True,
    #)



