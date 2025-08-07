# 🛑 Disaster Casualty Analysis

A Streamlit-based web app that uses image captioning and large language models (LLMs) to analyze disaster images and extract structured reports — including potential human casualties, environmental conditions, and infrastructure damage.

## 📸 Overview

This tool allows you to:
- Upload an image from a disaster scene.
- Automatically generate a descriptive caption using a BLIP image captioning model.
- Generate a detailed disaster report with structured information using a Groq-hosted LLM (GPT-based).

---

## 🚀 Features

- 🔍 **Automatic Image Captioning** with [BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base)
- 🤖 **LLM-based Disaster Report Generation** using [Groq](https://groq.com/)
- 🧠 Extracts:
  - Disaster type
  - Human/animal presence
  - Casualties or injured
  - Environmental conditions (e.g., smoke, fire, water, CO₂)
  - Infrastructure damage
  - Visibility conditions
- 📄 Includes a concise 3-line summary

---

## 🧰 Tech Stack

- **Frontend**: Streamlit
- **Vision Model**: [BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base) (by Salesforce)
- **Language Model**: GPT-style LLM hosted via [Groq](https://groq.com/)
- **Image Processing**: Pillow
- **Environment Management**: `python-dotenv`

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Soumya03007/Disaster-Casualty-Analysis.git
cd Disaster-Casualty-Analysis
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a .env file in the root directory:
```
HF_TOKEN=your_groq_api_token_here
```
### 4. Run the app
```bash
python -m streamlit run app.py
```

## 🙌 Acknowledgments
- Hugging Face for providing the models and hosting.

- Salesforce Research for the BLIP model.

- Groq for high-speed LLM inference.
