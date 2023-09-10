import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk
nltk.download('punkt')

def summarize_text(text, num_sentences = 5):
    parser = PlaintextParser.from_string(text,Tokenizer('english'))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return ''.join(str(sentence) for sentence in summary)

# Custom styles
st.markdown("""
    <style>
    .reportview-container {
        background-color: #f0f0f5;
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit app
st.markdown("<h1 style='text-align: center;'>Text Summarizer</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([2,1])

with col1:
    user_input = st.text_area("📝 Paste your text here for summarization:")

with col2:
    if st.button("🔍 Summarize"):
        if user_input:
            summarized = summarize_text(user_input, 3)
            st.subheader("📋 Summary:")
            st.write(summarized)
        else:
            st.write("🚨 Please input text to summarize.")