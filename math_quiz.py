
import streamlit as st
from PIL import Image

def show_math_image():
    st.markdown("## 📝 שאלון מתמטי לקביעת רמה")
    st.markdown("📌 העתיקו את השאלות למחברת, פתרו והביאו למורה.")

    image = Image.open("images/math_level_test.jpg")
    st.image(image, caption="תרגילים לקביעת רמת לימוד", use_column_width=True)

# בתוך הקוד הראשי:
show_math_image()

