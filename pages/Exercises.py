import streamlit as st
import streamlit.components.v1 as components
import base64

import streamlit as st
import streamlit.components.v1 as components
import base64
from PIL import Image
import io

st.set_page_config( page_title = "")
st.write(" #### Let's Relax for a while ", unsafe_allow_html=True)
#st.write(" # MENTAL MENTOR ", unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 




with open("exer.jpg", "rb") as f:
    img_content = f.read()

# Load image using PIL (Python Imaging Library)
image = Image.open(io.BytesIO(img_content))

# Define desired width and height for the image
width = 8000 # Set your desired width
height = 6000 # Set your desired height

# Resize the image
resized_image = image.resize((width, height))

# Display the resized image in Streamlit
st.image(resized_image, caption='', use_column_width=True)


  
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






def display_selected_exercise(exercise_name):
    if exercise_name == "Select your":
        display_exercise_page()
    elif exercise_name == "Meditate":
        display_meditate_page()
    elif exercise_name == "Mindfulness":
        display_mindfulness_page()
    elif exercise_name == "Hiking":
        display_hiking_page()



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 






def display_Select_your_exercise_page(): 
    st.write("Welcome! Please select a classifier.")
    st.title("Train Your Mind For Peace")
    st.subheader('Exercises are cool')

def display_meditate_page():
    st.title(" Meditate")
    # Import and execute meditate.py content here
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


def display_mindfulness_page():
    st.title("Mindfulness")
    st.write("Mindfullness")
    st.write("5 Steps to Mindfulness by Active Wellness:")
    st.write("It’s been said that mindfulness in the workplace can increase productivity and reduce stress. The question is, what is mindfulness? Mindfulness is a gentle effort to be aware moment to moment. It’s living in the present moment so all of your energy is directed to right now. In the present moment, your focus is clear, ideas flow freely and solutions arise.")

    st.write("You can train your brain to be more mindful. It’s just like strengthening a muscle. Try the following exercises to become more mindful:")

    st.write("1. LET GO OF PAST AND FUTURE THOUGHTS")

    st.write("If you let your mind wander into the past, you may waste your energy on regrets. If you think too much about the future, worries can drain your energy. Brief trips to the past and future are needed to deal with practical matters, but your power lies in the present moment.")

 

    st.write("2. ACCEPT THE PRESENT MOMENT")

    st.write("Accept the present moment just as it is without judgment so you can use your energy to directly handle the circumstance at hand. Mindfulness frees you from the tendency to react.")
    st.write("3. MEDITATE")

    st.write("One of the best ways to cultivate mindfulness is to focus on your breathing. Breathe deep into your belly and follow your breath all the way in and out. Notice your belly rise and fall. Notice the air passing through your nostrils. Expect your mind to wander and simply return your attention back to your breath. Try it at work for 3 minutes, three times a day to transform your day.")

 

    st.write("4. GET IN TOUCH WITH YOUR SENSES")

    st.write("Notice the sounds around you, the temperature of your skin, and the scents in the air.")
    st.write("Slow down to notice what’s going on around you in the moment.")

 

    st.write("5. PRACTICE MINDFULNESS DURING ROUTINE ACTIVITIES")

    st.write("Be mindful in moments such as brushing your teeth, taking a shower, eating, or walking.")
    st.write("For example, feel the ground against your feet while walking down the street. Take in the small details.")

    st.write("Mindfulness trains your brain to be more efficient, focused, and less distracted. It has also been shown to lower blood pressure, improve memory, lessen depression and anxiety, and is associated with increased athletic performance.")  

    st.write("Working mindfully is a feeling of being totally in the moment. There is joy, ease, and lightness in your work. Whether you are working at the office, spending time with your family, or getting in a workout, strive to live in the moment by practicing mindfulness.")
   
   
    # Import and execute mindfulness.py content here
    


    

def display_hiking_page():
    st.title("Hiking")
    st.write("Plan on walking 3 – 5 times per week.  Vary your speed and distances. Be sure to include long-distance and brisk walks – this could be part of your daily activities. If possible take the hilliest routes in your area.  Consider bringing a backpack with you so that you can get accustomed to carrying weight. Each week can add more weight to your pack – this also helps to train your upper body. Ideally use the same backpack that you’ll use when hiking so that you get used to it.")
    st.write("Take the stairs. This is important not only to build your cardiovascular endurance but will also strengthen your quads which will help you with the ascents throughout your hike.")
    st.write("BUILD YOUR CORE! It’s a major muscle but is often overlooked. Abdominal crunches are a go to for homework outs. Having a strong core (I’m not just talking six-pack abs) will help you more than you think.  When carrying a heavy backpack and as fatigue sets in, a strong core foundation is invaluable to get you up the mountain.")
    st.write("If you have a gym membership, take advantage of the incline setting on the treadmill and the stair climber. Look for other equipment geared towards building leg strength and getting your heart rate up. Progressive resistance training with the use of resistance bands doesn’t hurt. ")

    # Import and execute hiking.py content here

# Your Streamlit app starts here


exercises = st.sidebar.selectbox("", ("Select_your_exercise" , "Meditate", "Mindfulness", "Hiking"))

display_selected_exercise(exercises)



#st.write("# st.title("") ", unsafe_allow_html=True)

