import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json
st.title("Its Just Your Mind")


hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.write("In contemporary society, mental health issues have become increasingly prevalent, affecting individuals across diverse demographics. The multifaceted challenges faced by modern society contribute to a spectrum of mental health concerns that significantly impact individuals, communities, and broader societal well-being.One prominent issue revolves around the pervasive nature of stress in today's fast-paced lifestyle. The pressures of work, academic pursuits, financial instability, and societal expectations often culminate in heightened stress levels, leading to anxiety disorders and chronic stress-related conditions.Moreover, the pervasive influence of digital connectivity and social media presents its own set of challenges. While technology facilitates communication and access to information, excessive screen time and social media exposure contribute to feelings of isolation, comparison, and unrealistic standards, leading to depression, low self-esteem, and body image issues.")
st.write("Stress is any demand placed on your brain or physical body. Any event or scenario that makes you feel frustrated or nervous can trigger it.Anxiety is a feeling of fear, worry, or unease. While it can occur as a reaction to stress, it can also happen without any obvious trigger.Both stress and anxiety involve mostly identical symptoms, including: Trouble sleeping,digestive issues,difficulty concentrating,muscle tension,irritability or anger.")
st.write("Most people experience some feelings of stress and anxiety at some point, and that isn’t necessarily a “bad” thing. After all, stress and anxiety can sometimes be a helpful motivator to accomplish daunting tasks or do things you’d rather not (but really should).")
st.write("But unmanaged stress and anxiety can start to interfere with your daily life and take a toll on your mental and physical health.")
st.subheader("Mental Health Care Preventive Measures:")

st.write("**Education and Awareness:** Promoting mental health literacy to reduce stigma and increase awareness about mental health issues.")
st.write("**Early Intervention:** Identifying and addressing risk factors and symptoms at an early stage to prevent the escalation of mental health conditions.")
st.write("**Treatment and Support Services:**")

st.write("**Therapy and Counseling:** Psychological interventions such as cognitive-behavioral therapy (CBT), psychotherapy, and counseling to address emotional and behavioral issues.")
st.write("**Medication Management:** Prescription and management of medications for specific mental health conditions under the supervision of healthcare professionals.")
st.write("**Support Groups:** Peer support groups and community-based programs offering social and emotional support.")
st.write("**Access to Mental Health Professionals:**")

st.write("**Psychiatrists, Psychologists, and Therapists:** Qualified professionals who provide diagnosis, treatment, and therapy for various mental health conditions.Social Workers and Counselors: Professionals offering counseling and guidance for individuals and families facing mental health challenges.")
st.write("**Integrated Care:**")

st.write("**Collaborative Approaches:** Integration of mental health services with primary healthcare to address both physical and mental health needs comprehensively.")
st.write("**Holistic Treatment:** Emphasizing holistic approaches that consider social, cultural, and environmental factors influencing mental health.")
st.write("**Community Support and Advocacy:**")

st.write("**Community Resources:** Accessible mental health services and programs within local communities to provide support and care.")
st.write("**Advocacy and Policy Initiatives:** Efforts to promote mental health policies, destigmatize mental illness, and improve access to care at societal levels.")
st.write("**Crisis Intervention and Support:**")

st.write("**Hotlines and Helplines:** Immediate support and guidance during mental health crises or emergencies.")
st.write("**Crisis Intervention Teams:** Specialized teams providing on-site support during mental health crises.")


