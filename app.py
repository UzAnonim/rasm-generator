import streamlit as st
import requests
import base64

st.set_page_config(page_title="AI Rasm Generator", page_icon="🎨", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #6C63FF;'>🎨 AI Rasm Generator</h1>
    <p style='text-align: center; color: gray;'>Xayolingizdagi rasmni yarating!</p>
""", unsafe_allow_html=True)

token = "sizning_stability_keyingiz"

prompt = st.text_input("📝 Rasm tavsifini yozing (inglizcha):")

if st.button("🚀 Rasm yarat", use_container_width=True):
    if prompt:
        with st.spinner("⏳ Rasm yaratilmoqda..."):
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
            st.image(img_data, caption=prompt, use_column_width=True)
            st.success("✅ Rasm tayyor!")
    else:
        st.warning("⚠️ Iltimos, tavsif yozing!")
