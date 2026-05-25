import streamlit as st
import requests
import base64
from PIL import Image
import io

st.title("🎨 AI Rasm Generator")

token = "sk-LxSc5hMm7u5IneXtDJy3DLkbiUg1a8gsoucV5DX42knGxN6R"

prompt = st.text_input("Rasm tavsifini yozing (inglizcha):")

if st.button("Rasm yarat"):
    with st.spinner("Rasm yaratilmoqda..."):
        response = requests.post(
            "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image",
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            },
            json={
                "text_prompts": [{"text": prompt}],
                "height": 1024,

                "width": 1024,
            }
        )
        img_data = base64.b64decode(response.json()["artifacts"][0]["base64"])
        st.image(img_data)
