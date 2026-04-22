import streamlit as st
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("./final_model")
tokenizer = AutoTokenizer.from_pretrained("./final_model")

model.eval()

labels = [
    "Atheism",
    "Computer Graphics",
    "Windows OS Issues",
    "IBM PC Hardware",
    "Mac Hardware",
    "X Window System",
    "For Sale",
    "Cars",
    "Motorcycles",
    "Baseball",
    "Hockey",
    "Cryptography",
    "Electronics",
    "Medical",
    "Space",
    "Christianity",
    "Gun Politics",
    "Middle East Politics",
    "General Politics",
    "Religion Misc"
]

# 🎨 CSS لتكبير الخط
st.markdown("""
    <style>
    .big-title {
        font-size:40px !important;
        font-weight: bold;
    }
    .big-textarea textarea {
        font-size:20px !important;
    }
    .big-result {
        font-size:28px !important;
        font-weight: bold;
        color: #00c853;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🧠 Text Classification with BERT</div>', unsafe_allow_html=True)

text = st.text_area("Enter your text:", height=200)

if st.button("Predict"):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    with torch.no_grad():
        outputs = model(**inputs)

    pred = torch.argmax(outputs.logits, dim=1).item()

    st.markdown(
        f'<div class="big-result">Prediction: {labels[pred]}</div>',
        unsafe_allow_html=True
    )