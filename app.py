import streamlit as st
import pickle
import string

def preprocess_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    return text

# Load model and vectorizer
with open("spam_classifier.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("vectorizer.pkl", "rb") as vec_file:
    vectorizer = pickle.load(vec_file)

st.title("📱 SMS Spam Detector")

user_input = st.text_area("Enter your message:")

if st.button("Check Message"):
    if user_input.strip() == "":
        st.warning("Please enter a message to check.")
    else:
        processed = preprocess_text(user_input)
        vectorized = vectorizer.transform([processed])
        prediction = model.predict(vectorized)
        result = "🚫 Spam" if prediction[0] == 1 else "✅ Not Spam"
        st.subheader(result)
        
# Footer
st.divider()
st.markdown(
    "<p style='text-align: center;'>Made by <b>Anushka Joshi</b>.</p>", 
    unsafe_allow_html=True
)