import streamlit as st

st.set_page_config(page_title="Disaster Feature Extraction 🛑")

import os
from PIL import Image
from dotenv import load_dotenv
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
from huggingface_hub import InferenceClient

# Load environment variables
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

# Setup Groq inference client
client = InferenceClient(
    provider="groq",
    api_key=HF_TOKEN,
)

# Load BLIP model once
@st.cache_resource
def load_blip_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, blip_model = load_blip_model()

# Function to generate caption from image
def generate_caption(image: Image.Image) -> str:
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        out = blip_model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

# Function to create disaster report using Groq-hosted LLM
def generate_disaster_report(caption: str) -> str:
    prompt = f"""
📋 Disaster Report:
You are a disaster response analyst. Based on the following image description, extract structured disaster information.

Image Caption: "{caption}"

Return the following:

Disaster Type  
Human Presence  
Animal Presence  
Casualties or Injured  
Environmental Conditions (CO2, O2, smoke, water, fire, debris, vegetation)  
Infrastructure Damage  
Visibility  

End with a 3-line summary. Use "No Info" if uncertain.
"""

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error during inference: {str(e)}"

# Streamlit UI

st.title("📸 Disaster Analysis from Image")

uploaded_file = st.file_uploader("Upload a disaster image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("🖋 Generating image caption..."):
        caption = generate_caption(image)
        st.markdown(f"**🖋 Auto-Caption:** `{caption}`")

    with st.spinner("🔍 Generating disaster report..."):
        report = generate_disaster_report(caption)
        st.subheader("📝 Disaster Report:")
        st.write(report)
