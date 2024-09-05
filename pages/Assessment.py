import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder  # Importing LabelEncoder

st.title("Let's Get Predict Your Mind  ")
# Classifier selection from sidebar
classifiers = st.sidebar.selectbox("Used Classifier", ("SVC", "Random Forest", "NaiveBayes"))

# Load the dataset
data = pd.read_csv("survey.csv")
data.drop(columns=['Timestamp', 'Country', 'state', 'comments'], inplace=True)
data['dailylife_interfere'] = data['dailylife_interfere'].fillna("Don't know")
data['self_employed'] = data['self_employed'].fillna('No')

# Preprocess the data (clean, encode, etc.)
label_encoder = LabelEncoder()
for col in data.select_dtypes(include=[object]).columns:
    data[col] = label_encoder.fit_transform(data[col])

# Define the features and the target
X = data.drop("treatment", axis=1)
y = data["treatment"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1200)

# Function to get classifier
def get_classifier(clf_name):
    if clf_name == "SVC":
        return SVC(C=1.0)
    elif clf_name == "Random Forest":
        return RandomForestClassifier(n_estimators=100, max_depth=10, random_state=1200)
    elif clf_name == "NaiveBayes":
        return GaussianNB()

# Get the selected classifier
clf = get_classifier(classifiers)

# Train and predict
clf.fit(X_train, y_train)
y_pred_test = clf.predict(X_test)

# User input fields (rest of your code here)


st.write("1. Enter your age ")
age = st.number_input("Age",0,100)
st.write("2. Enter your gender ")
st.write("Female:0 , Male : 1 , Other:2")
Gender = st.number_input("Gender",0,2)
st.write("3. Are you self employed or not?")
st.write(" No:0 , Yes:1")
self_employed = st.number_input("Self employed",0,1)
st.write(" 4. Do you have a family history of mental illness?")
st.write(" No:0 , Yes:1")
family_history = st.number_input("Family history",0,1)
st.write("5. Did your mental discomfort interferes your field of activity in any means?")
st.write(" Often:0 , Rarely:1 , Never:2 , Sometimes:3 , Don't know:4")
dailylife_interfere = st.number_input("Activity field interfere",0,4)
st.write("6. Number of people you may interact in a day?")
no_interactions = st.number_input("no of interactions",0,1000)
st.write("7. Do you work remotely (outside of an office) at least 50% of the time?")
st.write(" No:0 , Yes:1")
remote_work = st.number_input("remote_work",0,2)
st.write("8. Do you experiance any pressure from your activity(study or work) field?")
st.write(" Yes:0 , No:1")
workorstudy_pressure = st.number_input("Field",0,1)
st.write("9. Does any mental health benefits provided in your field?")
st.write(" Yes:0 , Don't know:1 ,No:2")
benefits = st.number_input("benefits",0,2)
st.write("10. Are you aware of the mental health care programmes and benefits availed at your field?")
st.write(" NotSure:0 ,No:1 ,Yes:2")
care_options = st.number_input("Care options",0,2)
st.write("11. Do you attended any mental wellness program conducted ?")
st.write(" No:0,Don't Know:1,Yes:2")
wellness_program = st.number_input("Wellness program",0,2)
st.write("12. Does your department provide resources to learn more about mental health issues and how to seek help?")
st.write(" Yes:0,Don't know:1,Yes:2")
seek_help = st.number_input("Seek help",0,2)
st.write("13. Did your anonymity protected if you choose to take advantage of mental health treatment resources?")
st.write(" Yes:0 , Don't know:1 , N0:2")
anonymity= st.number_input("Anonymity",0,2)
st.write("14. How easy is it for you to take medical leave for a mental health condition?")
st.write(" Easy:0 , Don't know:1 ,Somewhat difficult:2 ,Very difficult:3 ,Very easy:4")
leave= st.number_input("Leave",0,4)
st.write("15. Do you feel bad on sharing your mental health issue with any one of your colleague?")
st.write(" No:0 ,Maybe:1 , Yes:2 ")
mental_health_consequence = st.number_input("Sharing to individual",0,2)
st.write("16. Do you feel bad on discussing your mental health issue with in your colleague group?")
st.write(" No:0 , Yes:1 , Maybe:2")
phys_health_consequence= st.number_input("Share with group of colleagues",0,2)
st.write("17. Would you be willing to discuss a mental health issue with your friends?")
st.write(" Some of them:0 , No:1 , Yes:2")
colleagues= st.number_input("Friends",0,2)
st.write("18. Would you be willing to discuss a mental health issue with your family?")
st.write(" Yes:0 , No:1 , Some of them:2")
family= st.number_input("Family",0,2)
st.write("19. Would you bring up any general mental health talks with a anyone in a casual talk?")
st.write(" No:0 , Yes:1 , Maybe:2")
in_a_group= st.number_input("Mental health talks",0,2)
st.write("20. Would you bring up your physical health issue with a anyone in a casual talk?")
st.write(" Maybe:0 , No:1 , Yes:2")
individual= st.number_input("physical health talks",0,2)
st.write("21. Do you feel that your colleagues and family takes mental health as seriously as physical health?")
st.write("mental vs physical Yes:0 , Don't know:1 , No:2")
mental_vs_physical= st.number_input("Mental vs physical",0,2)
st.write("22. Have you experianced negative consequences from colleagues on your mental health conditions?")
st.write(" No:0 , Yes:1")
obs_consequence= st.number_input("Negative consequence",0,1)

data1={'Age':age, 'Gender':Gender, 'self_employed':self_employed, 'family_history':family_history,
       'dailylife_interfere':dailylife_interfere, 'no_interactions':no_interactions, 'remote_work':remote_work, 'workorstudy_pressure':workorstudy_pressure,
       'benefits':benefits, 'care_options':care_options, 'wellness_program':wellness_program, 'seek_help':seek_help,
       'anonymity':anonymity, 'leave':leave, 'mental_health_consequence':mental_health_consequence,
       'phys_health_consequence':phys_health_consequence, 'colleagues':colleagues, 'family':family,
       'in_a_group':in_a_group, 'individual':individual,
       'mental_vs_physical':mental_vs_physical, 'obs_consequence':obs_consequence}
df2 = pd.DataFrame(data1,index=["Name"])
y_pred_test1 = clf.predict(df2)
if(y_pred_test1==0):
    st.write("YOU MAY BETTER GO FOR A TREATMENT.")
     # Adding graphical representation
    labels = ['Need Treatment', 'No Treatment']
    sizes = [1, 0]  # If user needs treatment
    st.video("https://www.youtube.com/watch?v=IC9DM7w-pm8")
    st.video("https://www.youtube.com/watch?v=AUom_FsLTMo")
    st.write("Some inspiration videos:")
    st.video("https://www.mayoclinic.org/diseases-conditions/mental-illness/diagnosis-treatment/drc-20374974")
    st.video("https://www.youtube.com/watch?v=-GXfLY4-d8w")
   
else:
    st.markdown("**<span style='color:green'>YOU DO NOT NEED ANY TREATMENT NOW. 😄</span>**", unsafe_allow_html=True)
    labels = ['Need Treatment', 'No Treatment']
    sizes = [0, 1]  # If user does not need treatment

    st.write("Just relax , watch the mentioned videos.....Also go through the exercices and tips provided. ")
    st.write("Some inspirational videos are:")
    st.video("https://www.youtube.com/watch?v=-GXfLY4-d8w")

    
   
# Calculate accuracy
acc = accuracy_score(y_test, y_pred_test)
st.write(f"Classifier Used: {classifiers}")
st.write(f"Accuracy Score: {acc:.2%}")

# Visualizing the results using Seaborn
fig, ax = plt.subplots()

# Create a confusion matrix or accuracy bar chart
sns.barplot(x=[classifiers], y=[acc * 100], ax=ax)
ax.set_title("Classifier Accuracy")
ax.set_ylabel("Accuracy (%)")
ax.set_ylim(0, 100)

# Display the graph
st.pyplot(fig)



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
