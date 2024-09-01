import streamlit as st
import streamlit.components.v1 as components
import base64



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

  
with open("yoga.gif", "rb") as f:
    img_content = f.read()
    data_url = base64.b64encode(img_content).decode("utf-8")

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
    )




st.write("Meditation is a great way to help calm the mind and body and get you out of the fight or flight zone. Meditation also works proactively by helping you learn to stay calm during stressful situations.")
st.write("1. Find a Quiet Space:")
st.write("2. Sit Comfortably:")
st.write("3. Relax & Close Your Eyes:")
st.write("4. Focus on Breathing:")
st.write("5. Stay Mind Present With No Judgement:")
st.write("Notice any thoughts that arise, but gently guide your attention back to your breath. Try to stay present and observe without judgment.")
st.write("6. Use Guided Meditation (Optional):")
st.write("You can use guided meditation apps or recordings that provide instructions and calming music.")
st.write("7. Start Small:")
st.write("Begin with short sessions, maybe 5-10 minutes, and gradually increase the duration as you get comfortable.")
st.write("8. Be Patient:")
st.write("Meditation takes practice. Don’t get discouraged if your mind wanders. It’s normal. Keep practicing.")
st.write("9. Experiment:")
st.write("Explore different meditation techniques like mindfulness, loving-kindness, body scan, or focused breathing to find what works best for you.")
st.write("10. Consistency:")
st.write("Aim to meditate regularly, even if it's for a short duration. Consistency is more important than duration.")
st.write("11. Posture and Relaxation:")
st.write("Maintain a comfortable posture and focus on relaxation. Tension in the body can distract from the meditation experience.")
st.write("12. Reflect:")
st.write("After the session, take a moment to reflect on how you feel. Notice any changes in your mood, stress levels, or mental clarity.")
st.write("13. Seek Guidance (if needed):")
st.write("If you find it challenging to meditate alone, consider joining a meditation group, attending classes, or seeking guidance from a meditation teacher.")
st.write("14. Practice Gratitude:")
st.write("End your session with gratitude. Acknowledge your efforts in taking time for self-care and appreciate the moment.")
