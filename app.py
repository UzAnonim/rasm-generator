import streamlit as st
import requests
import base64
from deep_translator import GoogleTranslator

st.set_page_config(page_title="AI Rasm Generator", page_icon="🎨")

st.markdown("""
    <h1 style='text-align: center; color: #6C63FF;'>🎨 AI Rasm Generator</h1>
    <p style='text-align: center; color: gray;'>O'zbekcha yozing — rasm chiqadi!</p>
""", unsafe_allow_html=True)

token = "sizning_stability_keyingiz"

prompt = st.text_input("📝 Tavsif yozing (o'zbekcha):")

if st.button("🚀 Rasm yarat", use_container_width=True):
    if prompt:
        with st.spinner("Tarjima qilinmoqda..."):
            translated = GoogleTranslator(source='auto', target='en').translate(prompt)
            st.info(f"🔤 Inglizcha: {translated}")

        with st.spinner("Rasm yaratilmoqda..."):
            response = requests.post(
                "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image",
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json"
                },
                json={
                    "text_prompts": [{"text": translated}],
                    "height": 1024,
                    "width": 1024,
                }
            )
            img_data = base64.b64decode(response.json()["artifacts"][0]["base64"])
            st.image(img_data, caption=prompt, use_column_width=True)
            st.success("✅ Rasm tayyor!")
    else:
        st.warning("⚠️ Tavsif yozing!")
