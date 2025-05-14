import streamlit as st
from openai import OpenAI

# מפתח API
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# פונקציה לסיכום
def summarize_text(text, language):
    prompt = f"Summarize the following text in {language}:\n\n{text}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].message.content

# ממשק משתמש בסיסי
st.title("📄 AI Multilingual Summarizer")

text_input = st.text_area("Enter your text:")
language = st.selectbox("Choose summary language:", ["English", "עברית", "العربية", "Français", "Español"])

if st.button("Summarize"):
    if text_input:
        summary = summarize_text(text_input, language)
        st.subheader(f"📝 Summary in {language}")
        st.write(summary)
    else:
        st.warning("Please enter text first.")
