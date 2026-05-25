import streamlit as st
import requests
import base64

st.set_page_config(page_title="AI Rasm Generator", page_icon="🎨", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #6C63FF;'>🎨 AI Rasm Generator</h1>
    <p style='text-align: center; color: gray;'>Xayolingizdagi rasmni yarating!</p>
""", unsafe_allow_html=True)

stability_token = "sizning_stability_keyingiz"
google_token = "sizning_google_translate_keyingiz"

prompt = st.text_input("📝 Rasm tavsifini yozing (o'zbekcha yoki inglizcha):")

if st.button("🚀 Rasm yarat", use_container_width=True):
    if prompt:
        with st.spinner("⏳ Tarjima qilinmoqda..."):
            translate = requests.post(
                f"https://translation.googleapis.com/language/translate/v2?key={google_token}",
                json={"q": prompt, "target": "en"}
            )
            translated = translate.json()["data"]["translations"][0]["translatedText"]
            st.info(f"🔤 Inglizcha: {translated}")

        with st.spinner("⏳ Rasm yaratilmoqda..."):
            response = requests.post(
                "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image",
                headers={
                    "Authorization": f"Bearer {stability_token}",
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
        st.warning("⚠️ Iltimos, tavsif yozing!")
